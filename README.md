# 🎙️ Audio Summary Skill - 录音转文字AI总结工具

> 把数小时的会议录音，变成结构清晰的会议纪要，只需几秒钟！

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![SiliconFlow](https://img.shields.io/badge/Powered%20by-SiliconFlow-green.svg)](https://cloud.siliconflow.cn/)

---

## ✨ 它能做什么？

你是不是也经常遇到这些情况？

- 😫 开会2小时，整理会议纪要要用一整天
- 😵 采访录音几小时，找关键信息听到头晕
- 🤯 线上课程录下来，却没时间重听做笔记
- 😤 手写记录总是漏掉重要内容

**Audio Summary Skill** 帮你一次性解决！

🎯 **一步完成**：录音 → 转文字 → AI智能总结

将数小时的音频，自动转成结构清晰的要点，**节省 90% 的时间**！

---

## 🚀 核心特性

### 🆓 完全免费开始
- ASR语音识别调用**不收费**
- 注册就送 **16元 API 使用金**
- AI总结可以用赠金完成

### ⚡ 极速处理
- 支持多种音频格式：MP3, WAV, M4A, OGG, FLAC...
- 智能分段，长录音也能轻松处理
- 批量处理整个文件夹

### 🧠 四种总结模式
| 模式 | 适用场景 |
|------|---------|
| **详细总结** | 会议记录、访谈整理 |
| **要点列表** | 快速浏览、决策参考 |
| **关键词** | 内容索引、标签提取 |
| **一句话** | 标题生成、快速分享 |

### 🔒 隐私安全
- 国内合规平台，数据不出境
- 不用于模型训练
- 企业级数据保护

---

## 💡 使用场景

```
会议场景：
├── 2小时录音 → 10分钟读完要点
├── 自动提取：决议事项/待办任务/责任人
└── 导出可直接归档或发邮件

采访场景：
├── 全程录音 → 精华观点提取
├── 按主题分段整理
└── 金句自动高亮

课程培训：
├── 直播录屏 → 知识点整理
├── 生成复习大纲
└── 重点时间戳定位
```

---

## 🎁 注册即领 16 元！

```
✅ 点击注册 → https://cloud.siliconflow.cn/i/q8iwvh5Z
✅ 完成实名认证
✅ 首页领取「认证专项礼」16元奖励券
✅ 开始免费使用！
```

---

## 📦 安装使用

### 方式一：直接在 Claude Code 中使用

如果你的 Claude Code 已配置 skills，直接启用即可：

```bash
# 安装技能到 Claude Code
cp -r audio-summary ~/.claude/skills/
```

然后在对话中说："帮我总结这个录音"，Claude 就会自动调用！

### 方式二：命令行使用

```bash
# 1. 克隆仓库
git clone https://github.com/yourusername/audio-summary.git
cd audio-summary

# 2. 设置 API Key
export SILICONFLOW_API_KEY="你的-api-key"

# 3. 运行！
python scripts/asr_summary_skill.py 会议录音.mp3 --summary-type points -o 会议纪要.md
```

### 方式三：Python 代码调用

```python
from scripts.asr_summary_skill import ASRSummarySkill

# 初始化
skill = ASRSummarySkill(api_key="你的-api-key")

# 处理单个文件
result = skill.process_audio("面试录音.mp3", summary_type="points")
print(result["summary"])

# 批量处理
results = skill.process_batch("./录音文件夹/")
```

---

## 🛠️ 技术栈

- **语音识别**：SiliconFlow SenseVoiceSmall (支持中英粤日韩)
- **AI总结**：Kimi-K2.5 Pro 模型
- **底层平台**：硅基流动 SiliconFlow

---

## 📊 成本说明

| 项目 | 费用 | 说明 |
|------|------|------|
| 语音识别 | **免费** | SiliconFlow ASR 目前不收费 |
| AI总结 | 约 ¥0.001-0.003/次 | 16元赠金可用数千次 |
| 总计 | **几乎为零** | 正常使用完全够用 |

---

## 🤝 贡献

欢迎提交 Issue 和 PR！让我们一起把这个工具做得更好。

---

## 📄 License

本项目采用 MIT 许可证 - 详见 [LICENSE.txt](LICENSE.txt) 文件

---

## 💬 有问题？

- 🐛 发现问题？提交 [Issue](../../issues)
- 📧 联系作者：[yonghui.qi9862@gmail.com]
- ⭐ 觉得好用？点个 Star 支持一下！

---

**让会议记录不再头疼，让知识获取更加高效！** 🚀
