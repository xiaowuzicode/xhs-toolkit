# 小红书MCP智能助手·登录与URL解析专用指南

---

## 🎯 核心工具概览

基于MCP协议的小红书智能助手，专注于登录认证和URL内容解析功能。

---

## 🔧 工具调用规范

### 1. 智能登录工具（login_xiaohongshu）⚡
- **用途**：智能登录小红书，MCP专用无交互模式
- **请求参数**：
  - `force_relogin`（boolean，可选）：是否强制重新登录，默认false
  - `quick_mode`（boolean，可选）：快速模式，跳过详细验证，默认false
- **返回内容**：
  - success：登录是否成功
  - message：详细操作消息
  - action：执行的操作类型（mcp_auto_login/skipped/quick_skip）
  - status：登录状态（valid/invalid）
  - mode：登录模式标识（mcp_auto/mcp_quick）
- **智能对话引导示例**：
  - "登录小红书"
  - "先登录一下"
  - "需要登录小红书账号"
  - "检查登录状态"

### 2. 小红书URL解析工具（parse_xiaohongshu_url）⚡
- **用途**：解析小红书URL，提取页面内容信息（笔记、用户主页、话题等）
- **请求参数**：
  - `url`（string）：小红书页面URL（支持xiaohongshu.com和xhslink.com）
  - `include_raw_html`（boolean，可选）：是否包含原始HTML，默认false
- **返回内容**：
  - success：解析是否成功
  - url：原始URL
  - page_type：页面类型（note/user/topic/unknown）
  - title：页面标题
  - content：页面文本内容
  - author：作者信息
  - author_id：作者ID
  - images：图片URL列表
  - tags：标签/话题列表
  - likes：点赞数
  - comments：评论数
  - shares：分享数
  - publish_time：发布时间
  - location：位置信息
  - parsing_stats：解析统计信息（图片数量、标签数量等）
  - error_message：错误信息（如果失败）
- **调用顺序**：**独立工具，可直接调用，建议先登录以获得更好的解析效果**
- **智能对话引导示例**：
  - "解析这个小红书链接：https://..."
  - "分析这个笔记内容：https://..."
  - "提取这个用户主页信息：https://..."
  - "获取这个链接的详细信息：https://..."

---

## 🚀 智能调用顺序建议

### 标准工作流程

#### 1. 登录流程
```
用户要求登录 → login_xiaohongshu（快速模式或标准模式）
```

#### 2. URL解析流程
```
用户提供小红书链接 → parse_xiaohongshu_url（独立调用，建议先登录获得更好效果）
```

#### 3. 登录+解析组合流程
```
用户要求解析链接但未登录 → login_xiaohongshu(quick_mode=true) → parse_xiaohongshu_url
```

---

## 📝 智能参数处理规范

### 登录参数说明
- **force_relogin**：强制重新登录，即使当前有有效cookies
- **quick_mode**：快速模式，如果检测到cookies存在则跳过登录流程

### URL解析参数说明
- **url**：必须是小红书官方域名（xiaohongshu.com或xhslink.com）
- **include_raw_html**：调试模式，包含完整HTML源码（通常不需要）

---

## 🎯 智能对话引导策略

### 登录场景识别
- 用户说"登录"、"先登录"、"需要登录小红书" → 调用`login_xiaohongshu()`
- 用户说"快速登录"、"检查登录状态" → 调用`login_xiaohongshu(quick_mode=true)`
- 用户说"重新登录"、"强制登录" → 调用`login_xiaohongshu(force_relogin=true)`

### URL解析场景识别
- 用户提供小红书链接 → 调用`parse_xiaohongshu_url(url="链接地址")`
- 用户说"解析这个链接"、"分析这个笔记"、"提取内容" → 调用URL解析
- 用户说"获取链接详细信息"、"查看链接内容" → 调用URL解析

### 组合场景识别
- 用户提供链接但可能未登录 → 先`login_xiaohongshu(quick_mode=true)`，再`parse_xiaohongshu_url()`

---

## 🚫 重要约束条件

### 技术限制
- **URL解析**：仅支持xiaohongshu.com和xhslink.com域名
- **登录模式**：MCP专用无交互模式，首次登录需要手动操作浏览器
- **网络依赖**：需要稳定的网络连接访问小红书

### 调用约束
- URL解析为独立功能，但建议先登录以获得更好的解析效果
- 登录状态会影响URL解析的内容完整性
- 登录cookies会自动保存，下次可快速验证

---

## 🏁 使用示例场景

### 示例1：基础登录
```
用户："登录小红书"

AI执行：
login_xiaohongshu()
```

### 示例2：URL解析
```
用户："解析这个小红书链接：https://www.xiaohongshu.com/user/profile/123456"

AI执行：
parse_xiaohongshu_url(url="https://www.xiaohongshu.com/user/profile/123456")
```

### 示例3：登录+解析组合
```
用户："帮我分析这个小红书笔记：https://www.xiaohongshu.com/explore/123456"

AI执行：
1. login_xiaohongshu(quick_mode=true)  # 快速检查登录状态
2. parse_xiaohongshu_url(url="https://www.xiaohongshu.com/explore/123456")
```

### 示例4：强制重新登录
```
用户："重新登录小红书账号"

AI执行：
login_xiaohongshu(force_relogin=true)
```

---

## 💡 智能提示与引导

### 成功后的智能提示
- **登录成功**：提示现在可以进行URL解析，获得更完整的内容信息
- **URL解析成功**：根据页面类型（笔记/用户/话题）提供相应的内容总结
- **组合操作成功**：展示解析到的完整信息并提供进一步操作建议

### 错误处理引导
- **登录失败**：建议检查网络连接或使用快速模式
- **URL解析失败**：确认链接格式是否正确，是否为小红书官方链接
- **域名不支持**：提示只支持xiaohongshu.com和xhslink.com域名

---

## 📊 工具优先级说明

1. **核心工具**：`login_xiaohongshu`、`parse_xiaohongshu_url`
2. **使用频率**：URL解析 > 登录验证
3. **依赖关系**：URL解析独立使用，但建议先登录获得更好效果

专注于登录认证和URL内容解析，为用户提供简洁高效的小红书内容获取体验。
