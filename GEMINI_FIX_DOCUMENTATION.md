# Fix for Gemini Model Template Parsing Issue

## Problem Summary

When running experiments with Gemini models (e.g., `gemini-2.5-flash-lite`), the pipeline consistently failed after the context diagram was created, when entering the container analysis phase with the first expert agent. The error was:

```
KeyError: 'Input to ChatPromptTemplate is missing variables {\'\\n    "level"\'}.  
Expected: [\'\\n    "level"\', \'messages\'] Received: [\'messages\']
```

**Key observation**: The pipeline worked fine with GPT models but failed with Gemini models.

## Root Cause Analysis

The issue was in the `agent_node` function in `src/c4modeler/agents.py`. The function was using Python f-strings to embed dynamic content directly into the system prompt:

```python
# OLD CODE (PROBLEMATIC)
system_prompt = (
    "You are a member of an expert team...\n"
    f"Your current task is to analyze the provided system brief for the **C4 {state['level']} level**.\n"
    f"{state['context']}\n"
    "Your specific role is as follows:\n---\n"
    f"{agent.persona}\n---\n"
    "..."
)
```

### Why did this cause problems with Gemini but not GPT?

1. **Gemini's response format**: Gemini models tend to structure their responses with JSON or YAML formatting, including curly braces:
   ```json
   {
       "level": "container",
       "system": {...}
   }
   ```

2. **Message history propagation**: These responses get added to the conversation's message history

3. **Template parsing conflict**: When the next agent's turn comes:
   - The `ChatPromptTemplate` receives the conversation history via `MessagesPlaceholder`
   - The template parser scans ALL content (including historical messages) for template variables
   - It sees `{` followed by `"level"` in the previous messages
   - It interprets `{\n    "level"` as a template variable that needs to be provided
   - Since this "variable" isn't in the invoke() arguments, it raises a KeyError

4. **Why GPT didn't trigger this**: GPT models typically format their responses with more natural language and fewer JSON-style curly braces in the initial analysis phases, so the template parser didn't encounter these patterns.

## The Solution

Changed the `agent_node` function to use **proper template variables** instead of f-string embedding:

```python
# NEW CODE (FIXED)
system_prompt = (
    "You are a member of an expert team...\n"
    "Your current task is to analyze the provided system brief for the **C4 {level} level**.\n"
    "{context}\n"
    "Your specific role is as follows:\n---\n"
    "{persona}\n---\n"
    "..."
)

# Pass all dynamic content as template variables
response = chain.invoke({
    "messages": state["messages"],
    "level": state["level"],
    "context": state["context"],
    "persona": agent.persona
})
```

### Why this fixes the issue:

1. **Clear variable boundaries**: The template parser knows exactly which variables to expect: `{level}`, `{context}`, `{persona}`, and `{messages}`
2. **Message content isolation**: Content within the messages themselves is NOT parsed for variables
3. **Consistent behavior**: Works the same way regardless of what content the LLM generates
4. **Best practice**: This is the recommended approach in LangChain documentation

## Files Modified

- `src/c4modeler/agents.py`: 
  - Updated `agent_node` function to use template variables (lines ~105-131)
  - Added `strip_markdown_code_fences()` utility function (lines ~42-66)
  - Updated `yaml_structure_node` to clean code fences (lines ~295-348)
  - Updated `plantuml_diagram_node` to clean code fences (lines ~387-410)

## Additional Issue: Markdown Code Fences in YAML/PlantUML Output

### Problem
After fixing the template parsing issue, a second problem emerged: Gemini models wrap their YAML and PlantUML output in markdown code fences:

```yaml
level: container
...
```

This caused the YAML parser to fail with: `found character '`' that cannot start any token`

### Solution
Added a `strip_markdown_code_fences()` utility function that removes markdown code fences from LLM output before:
- Storing YAML definitions
- Storing PlantUML diagram code

This ensures the YAML parser receives clean YAML and the diagram code is properly formatted.

## Verification

The fixes can be tested by:
1. Running `python test_gemini_fix.py` to verify template handling
2. Running `python test_markdown_fence_stripping.py` to verify code fence cleaning
3. Running experiments with Gemini models (should now complete successfully through all C4 levels)
4. Checking that GPT models still work (they should, as these fixes are backward compatible)

## Why Other Functions Weren't Affected

Other functions like `report_generator_node`, `sequential_analysis_node`, `generate_yaml_node`, and `generate_plantuml_node` were already using proper template variables and passing content via dictionary arguments to `invoke()`, so they didn't have this issue.

## Prevention

To prevent similar issues in the future:

1. **Always use template variables** when working with `ChatPromptTemplate`
2. **Never use f-strings** to embed content that could contain user-generated or LLM-generated text
3. **Pass all dynamic content** as dictionary arguments to `invoke()`
4. **Test with multiple LLM providers** as they have different output formatting styles

## Related Best Practices

From LangChain documentation:
- Use `{variable_name}` syntax in prompt templates
- Pass variables as dictionary to `invoke()`
- Use `MessagesPlaceholder` for conversation history
- Escape literal curly braces with double braces: `{{literal text}}`
