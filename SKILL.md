---
name: audio-summary
description: This skill provides audio transcription and text summarization capabilities using SiliconFlow API. It should be used when users need to convert audio recordings (meetings, interviews, etc.) into text and generate structured summaries.
license: Complete terms in LICENSE.txt
---

# Audio Summary Skill

This skill provides audio transcription and text summarization capabilities using SiliconFlow API.

## Overview

The Audio Summary Skill enables automated transcription of audio files and generation of structured summaries. It supports various audio formats and multiple summary types.

## When to Use

Use this skill when you need to:
- Transcribe meeting recordings to text
- Generate summaries of interviews or discussions
- Batch process multiple audio files
- Extract key points from audio content

## Prerequisites

Before using this skill, you must obtain a SiliconFlow API Key:

1. Visit https://cloud.siliconflow.cn/i/q8iwvh5Z to register
2. Complete real-name verification
3. Claim your 16 RMB "Authentication Reward Coupon" from the homepage
4. Generate your API Key

## Usage

### Python API

```python
from scripts.asr_summary_skill import ASRSummarySkill

# Initialize with your API key
skill = ASRSummarySkill(api_key="your-api-key")

# Process a single audio file
result = skill.process_audio("meeting.mp3", summary_type="points")
print(result["transcription"])  # Full transcription
print(result["summary"])        # Structured summary

# Batch process a folder
results = skill.process_batch("./recordings/", summary_type="general")
```

### Command Line

```bash
# Single file
python scripts/asr_summary_skill.py meeting.mp3 --api-key "your-key" --summary-type points -o summary.md

# Batch processing
python scripts/asr_summary_skill.py ./recordings/ --batch --api-key "your-key" -o results.md

# Using environment variable
export SILICONFLOW_API_KEY="your-api-key"
python scripts/asr_summary_skill.py meeting.mp3
```

## Summary Types

- `general`: Detailed summary preserving key information
- `keywords`: Extract keywords and key phrases
- `points`: Organize content into bullet points
- `short`: One-sentence brief summary

## Supported Audio Formats

- MP3, WAV, M4A, OGG, FLAC, AAC, WMA

## Configuration

The skill uses the following SiliconFlow models:
- **ASR Model**: `FunAudioLLM/SenseVoiceSmall` (audio transcription)
- **Summary Model**: `Pro/moonshotai/Kimi-K2.5` (text summarization)

## Scripts

- `scripts/asr_summary_skill.py` - Main skill implementation with ASRSummarySkill class
