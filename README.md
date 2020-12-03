# MyBlog
一、关于前端
- 前端使用的Bootstrap框架，导航栏做了一点修改，二级导航原来需要点击才可显示，改成了浮动显示。
- 轮播图调用了不同的图片api和文字api，每次刷新就会更新。
- 首页个人信息、标签云、归档和文章都使用的Bootstrap的卡片。
- 最新评论和最热文章使用了滑动门和列表组的结合。
- 标签云的标签颜色、文章详情页标签颜色和评论框的显示与隐藏均使用Jquery实现。
- 点赞功能使用Vue发送Ajax请求，使用layui实现弹窗效果。

二、关于后端
- 评论表单使用Django自带的ModelForm。
- 发送邮件使用Django自带的send_mail()和send_mass_mail()，同时使用Celery异步发送邮件。
- 分类、归档、标签云、最新评论和最热文章、评论都是通过Django的自定义模板标签实现的。
- 文章和评论的创建时间显示格式使用了Django的自定义过滤器。
- 网站搜索使用django-haystack，whoosh作为搜索引擎，jieba作为分词工具。
- 文章后台markdown编辑器使用的django-mdeditor。
- 分页使用Django自带的Pagination类。
- 网站后台使用simpleui美化。
