#!/usr/bin/env python3
"""
ASR + 总结 Skill
将音频转录和文本总结能力封装在一起

使用方法:
from asr_summary_skill import ASRSummarySkill

skill = ASRSummarySkill(api_key="your-api-key")
# 直接处理音频并获取总结
result = skill.process_audio("audio.mp3")

============================================
【重要】使用前请先获取 API Key：
请到 https://cloud.siliconflow.cn/i/q8iwvh5Z 注册登录，获取 API Key。
注册实名认证后，首页-认证专项礼-领取 16 元「认证奖励券」。
领取成功后再发起请求。
============================================
"""

import argparse
import os
import sys
from pathlib import Path
import requests
from typing import Optional, Dict, Any


class ASRSummarySkill:
    """
    ASR + 总结 Skill
    提供音频转录和文本总结的一体化功能
    """
    
    # SiliconFlow API 配置
    DEFAULT_MODEL = "FunAudioLLM/SenseVoiceSmall"
    API_URL = "https://api.siliconflow.cn/v1/audio/transcriptions"
    CHAT_URL = "https://api.siliconflow.cn/v1/chat/completions"
    
    # 总结用的模型
    SUMMARY_MODEL = "Pro/moonshotai/Kimi-K2.5"
    
    def __init__(self, api_key: str = None, model: str = None):
        """
        初始化 Skill
        
        Args:
            api_key: SiliconFlow API Key（必填）
            model: ASR 模型名称，如果不提供则使用默认
        """
        self.api_key = api_key
        self.model = model or self.DEFAULT_MODEL
        
        if not self.api_key:
            raise ValueError(
                "请提供 SiliconFlow API Key。\n"
                "请先访问 https://cloud.siliconflow.cn/i/q8iwvh5Z 注册并获取 API Key。\n"
                "注册实名认证后，首页-认证专项礼-领取 16 元「认证奖励券」。"
            )
        
    def transcribe(self, audio_file: str) -> str:
        """
        转录音频文件为文字
        
        Args:
            audio_file: 音频文件路径
            
        Returns:
            转录后的文字
        """
        file_path = Path(audio_file)
        if not file_path.exists():
            raise FileNotFoundError(f"文件不存在: {audio_file}")
        
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        
        with open(file_path, "rb") as f:
            files = {
                "file": (file_path.name, f),
                "model": (None, self.model)
            }
            
            response = requests.post(
                self.API_URL,
                headers=headers,
                files=files,
                timeout=120
            )
            response.raise_for_status()
            result = response.json()
            return result.get("text", "")
    
    def summarize(self, text: str, summary_type: str = "general") -> str:
        """
        对文本进行总结
        
        Args:
            text: 需要总结的文本
            summary_type: 总结类型 (general/keywords/points/short)
            
        Returns:
            总结后的文本
        """
        prompts = {
            "general": "请对以下内容进行详细总结，保留关键信息：",
            "keywords": "请提取以下内容的关键词和关键短语：",
            "points": "请将以下内容整理成要点列表：",
            "short": "请用一句话简要概括以下内容："
        }
        
        prompt = prompts.get(summary_type, prompts["general"])
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.SUMMARY_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个专业的文本总结助手，擅长提取关键信息。"
                },
                {
                    "role": "user",
                    "content": f"{prompt}\n\n{text}"
                }
            ],
            "stream": False
        }
        
        response = requests.post(
            self.CHAT_URL,
            headers=headers,
            json=data,
            timeout=120
        )
        response.raise_for_status()
        result = response.json()
        
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        return ""
    
    def process_audio(self, audio_file: str, summary_type: str = "general") -> Dict[str, str]:
        """
        一键处理：转录音频并总结
        
        Args:
            audio_file: 音频文件路径
            summary_type: 总结类型
            
        Returns:
            包含转录文本和总结的字典
            {
                "transcription": "转录内容",
                "summary": "总结内容",
                "audio_file": "音频文件路径"
            }
        """
        print(f"🎤 正在转录音频: {Path(audio_file).name}")
        transcription = self.transcribe(audio_file)
        print("✅ 转录完成")
        
        if transcription:
            print(f"📝 正在生成{summary_type}总结...")
            summary = self.summarize(transcription, summary_type)
            print("✅ 总结完成")
        else:
            summary = ""
        
        return {
            "transcription": transcription,
            "summary": summary,
            "audio_file": audio_file
        }
    
    def process_batch(self, folder: str, summary_type: str = "general") -> list:
        """
        批量处理文件夹中的音频文件
        
        Args:
            folder: 文件夹路径
            summary_type: 总结类型
            
        Returns:
            处理结果列表
        """
        folder_path = Path(folder)
        if not folder_path.exists():
            raise FileNotFoundError(f"文件夹不存在: {folder}")
        
        # 支持的音频格式
        supported = {'.mp3', '.wav', '.m4a', '.ogg', '.flac', '.aac', '.wma'}
        audio_files = []
        for ext in supported:
            audio_files.extend(folder_path.glob(f"*{ext}"))
            audio_files.extend(folder_path.glob(f"*{ext.upper()}"))
        
        results = []
        total = len(audio_files)
        
        for i, audio_file in enumerate(audio_files, 1):
            print(f"\n[{i}/{total}] 处理: {audio_file.name}")
            try:
                result = self.process_audio(str(audio_file), summary_type)
                results.append(result)
            except Exception as e:
                print(f"❌ 处理失败: {e}")
                results.append({
                    "transcription": "",
                    "summary": "",
                    "audio_file": str(audio_file),
                    "error": str(e)
                })
        
        return results


def main():
    """命令行入口"""
    
    # 显示说明
    print("=" * 60)
    print("📢 使用前请确保已获取 SiliconFlow API Key")
    print("=" * 60)
    print("请访问: https://cloud.siliconflow.cn/i/q8iwvh5Z")
    print("注册并获取 API Key，实名认证后可领取 16 元认证奖励券")
    print("=" * 60)
    print()
    
    parser = argparse.ArgumentParser(description="ASR + 总结 Skill")
    parser.add_argument("audio", help="音频文件或文件夹路径")
    parser.add_argument("--api-key", help="SiliconFlow API Key")
    parser.add_argument("--summary-type", 
                       choices=["general", "keywords", "points", "short"],
                       default="general",
                       help="总结类型")
    parser.add_argument("--batch", action="store_true", help="批量处理文件夹")
    parser.add_argument("--output", "-o", help="输出文件路径")
    
    args = parser.parse_args()
    
    # 获取 API Key
    api_key = args.api_key or os.environ.get("SILICONFLOW_API_KEY")
    
    skill = ASRSummarySkill(api_key=api_key)
    
    if args.batch:
        results = skill.process_batch(args.audio, args.summary_type)
        
        # 打印结果
        for r in results:
            print(f"\n{'='*50}")
            print(f"文件: {Path(r['audio_file']).name}")
            print(f"{'='*50}")
            print(f"【转录内容】\n{r['transcription'][:500]}...")
            print(f"\n【总结】\n{r.get('summary', '')}")
        
        # 保存到文件
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                for r in results:
                    f.write(f"\n{'='*50}\n")
                    f.write(f"文件: {Path(r['audio_file']).name}\n")
                    f.write(f"{'='*50}\n")
                    f.write(f"【转录内容】\n{r['transcription']}\n\n")
                    f.write(f"【总结】\n{r.get('summary', '')}\n\n")
            print(f"\n结果已保存到: {args.output}")
    else:
        result = skill.process_audio(args.audio, args.summary_type)
        
        print(f"\n{'='*50}")
        print("【转录内容】")
        print(result["transcription"])
        print(f"\n{'='*50}")
        print("【总结】")
        print(result["summary"])
        
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(f"文件: {result['audio_file']}\n\n")
                f.write(f"【转录内容】\n{result['transcription']}\n\n")
                f.write(f"【总结】\n{result['summary']}\n")
            print(f"\n结果已保存到: {args.output}")


if __name__ == "__main__":
    main()
