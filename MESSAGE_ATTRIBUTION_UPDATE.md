# Multi-Agent Message Attribution Update

## Overview

Updated the multi-agent collaboration system to properly attribute messages to their generating agents and create more natural agent-to-agent conversations.

## Problem

Previously, all agent messages were stored as `AIMessage` objects without proper attribution. This meant:
- ❌ No way to identify which agent said what
- ❌ Agents saw previous messages as "AI" responses, not as peer collaborators
- ❌ Less natural multi-agent dialogue

## Solution

Implemented **message name attribution** and **message type conversion** to create natural multi-agent conversations.

### Key Changes

**1. Message Name Attribution**
```python
# Each agent message now has a 'name' field identifying the speaker
sanitized_name = re.sub(r"[^a-zA-Z0-9_-]", "_", agent.name)
named_message = AIMessage(content=response.content, name=sanitized_name)
```

**2. AIMessage → HumanMessage Conversion**
```python
# Convert AI messages to Human messages so agents see each other as collaborators
converted_messages = []
for msg in messages:
    if isinstance(msg, AIMessage):
        # Convert AI message to Human message, preserving the agent's name
        converted_messages.append(HumanMessage(content=msg.content, name=msg.name))
    else:
        converted_messages.append(msg)
```

## How It Works

### Before (Old System)

```
Turn 1 - Product Owner:
  Sees: [HumanMessage("Let's analyze...")]
  Generates: AIMessage("From business perspective...")
  
Turn 2 - Architect:
  Sees: [HumanMessage("Let's analyze..."), 
         AIMessage("From business perspective...")]  ← Sees as AI response
  Generates: AIMessage("From technical perspective...")
```

### After (New System)

```
Turn 1 - Product Owner:
  Sees: [HumanMessage("Let's analyze...")]
  Generates: AIMessage("From business perspective...", name="Product_Owner")
  
Turn 2 - Architect:
  Sees: [HumanMessage("Let's analyze..."),
         HumanMessage("From business perspective...", name="Product_Owner")]  ← Sees as human collaborator!
  Generates: AIMessage("From technical perspective...", name="Architect")
```

## Benefits

### ✅ Message Attribution
- Every message has a `name` field identifying the speaker
- Easy to trace which agent said what
- Better for debugging and analysis
- Enables agent-specific filtering

### ✅ Natural Collaboration
- Agents see each other's messages as `HumanMessage` (peer input)
- Creates more natural multi-agent dialogue
- Agents respond as if collaborating with humans
- Better aligns with how LLMs are trained (human-AI conversations)

### ✅ Improved Agent Behavior
- Agents more likely to engage naturally with "human" peers
- Reduces "AI acknowledging AI" artifacts
- More diverse perspectives since agents see peer input, not AI output
- Better conversation flow

## Technical Details

### Message Name Field

From [LangChain Messages Documentation](https://docs.langchain.com/oss/python/langchain/messages):

```python
human_msg = HumanMessage(
    content="Hello!",
    name="alice",  # Optional: identify different users
    id="msg_123",  # Optional: unique identifier for tracing
)
```

The `name` field:
- Identifies different speakers in a conversation
- Preserved across message type conversions
- Behavior varies by provider (some use for tracking, others ignore)
- Useful for multi-agent systems (our use case!)

### Message Type Conversion

The conversion happens **at read time**, not write time:
1. Messages are stored as `AIMessage` (with agent name)
2. When reading for next agent, they're converted to `HumanMessage`
3. This creates natural "human-to-human" conversation flow
4. Original messages remain in state for traceability

### Code Location

**File**: `src/c4modeler/agents.py`  
**Function**: `agent_node()`  
**Lines**: ~216-279

## Example Conversation

### Message Flow

```python
# Round 1
State: [HumanMessage("Analyze clinic system...")]

Product_Owner generates:
  → AIMessage("Need patient portal, EHR integration...", name="Product_Owner")

Architect sees:
  [HumanMessage("Analyze clinic system..."),
   HumanMessage("Need patient portal, EHR integration...", name="Product_Owner")]
  
Architect generates:
  → AIMessage("Microservices with API gateway...", name="Architect")

DevOps sees:
  [HumanMessage("Analyze clinic system..."),
   HumanMessage("Need patient portal...", name="Product_Owner"),
   HumanMessage("Microservices with API gateway...", name="Architect")]
```

## LangSmith Tracing

With named messages, LangSmith traces now show:
- **Speaker identification** for each message
- **Agent interaction patterns** clearly visible
- **Conversation flow** easier to analyze
- **Better debugging** when issues occur

## Backward Compatibility

✅ **Fully backward compatible**
- Existing code continues to work
- No changes to state schema
- No changes to external APIs
- Only internal message handling updated

## Testing

To verify the changes work:

```python
# Run a simple experiment
python run_experiments.py --experiment role_ablation --temperature 0.5

# Check LangSmith traces
# Messages should now show 'name' field with agent roles
# Conversation should look more natural
```

## Future Enhancements

Potential improvements enabled by this change:

1. **Agent-specific analysis**
   - Track which agents contribute most
   - Identify agent interaction patterns
   - Measure individual agent impact

2. **Dynamic turn-taking**
   - Agents could request specific peers to respond
   - Conditional conversation flows
   - Agent-initiated discussions

3. **Speaking order experiments**
   - Already supported by role_interaction experiment
   - Now with proper attribution for analysis

4. **Conversation visualization**
   - Build agent interaction diagrams
   - Visualize information flow
   - Identify collaboration bottlenecks

## References

- [LangChain Messages Documentation](https://docs.langchain.com/oss/python/langchain/messages)
- [HumanMessage API Reference](https://reference.langchain.com/python/langchain/messages/#langchain.messages.HumanMessage)
- [AIMessage API Reference](https://reference.langchain.com/python/langchain/messages/#langchain.messages.AIMessage)

---

**Date**: October 27, 2025  
**Version**: 1.0  
**Status**: Implemented and tested  
**Impact**: Core system enhancement for better multi-agent collaboration
