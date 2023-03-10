from pyecharts import options as opts
from pyecharts.charts import Sankey,TreeMap,Tab,Line,Grid
from pyecharts.globals import ThemeType


def History(width,height):
    # 显示的标签，并设置标签的深度
    nodes = [
        {"name": "GPT-1(2018)","depth":0},
        {"name": "More Parameters","depth":0},
        {"name": "GPT-2(2019)","depth":1},
        {"name": "GPT-3(2020)","depth":2},
        {"name": "ChatGPT(2022)","depth":3},
        {"name": "RLHF","depth":2},
        {"name": "TAMER","depth":2}
    ]
    # 标签之间的对应关系和值
    links = [
        {"source": "GPT-1(2018)", "target": "GPT-2(2019)", "value": 3},
        {"source": "More Parameters", "target": "GPT-2(2019)", "value": 1},
        {"source": "GPT-2(2019)", "target": "GPT-3(2020)", "value": 4},
        {"source": "More Parameters", "target": "GPT-3(2020)", "value": 1},
        {"source": "GPT-3(2020)", "target": "ChatGPT(2022)", "value": 5},
        {"source": "RLHF", "target": "ChatGPT(2022)", "value": 1},
        {"source": "TAMER", "target": "ChatGPT(2022)", "value": 1},
    ]

    c = (
        Sankey(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
        .add(
            # 图例标识
            "History",
            # 需要表示的标签
            nodes,
            # 便签之间的对应关系
            links,

            # 设置边框格式
            itemstyle_opts=opts.ItemStyleOpts(border_color='#ffffff'),
            # 设置线条格式
            linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
            # 设置label标签格式
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_series_opts(
            opts.TextStyleOpts(font_size=16), )
        .set_global_opts(
            # 浮动提示框设置
            tooltip_opts=opts.TooltipOpts(is_show_content=False),
            # 标题设置
            title_opts=opts.TitleOpts(title="ChatGPT",title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
            # 右上角贴图
            graphic_opts=[
                opts.GraphicImage(
                    graphic_item=opts.GraphicItem(
                        id_="logo", right=20, top=20, z=-10, bounding="raw", origin=[75, 75]
                    ),
                    graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                        image="ChatGPT.png",
                        width=100,
                        height=100,
                        opacity=0.4,
                    ),
                )
            ],
            # 工具箱功能是否显示
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            # 图例设置
            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=20))
        )
    )
    c = (
        Grid(init_opts=opts.InitOpts(width=width,height=height))
        .add(
            chart=c,
            grid_opts=opts.GridOpts(pos_left="5%", pos_right="4%", pos_bottom="5%"),
        )
    )
    return c

def Parameters(width,height):

    # 所使用的数据
    x_data=['GPT-1','GPT-2','GPT-3','ChatGPT']
    y_data_1=[12,48,96,192]
    y_data_2=[1.17,15,1750,3500]
    y_data_3=[5,40,46000,92000]

    c=(
        Line()
        .add_xaxis(xaxis_data=x_data)
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="参数量（亿）",
                type_="value",
                axislabel_opts=opts.LabelOpts(formatter="{value} 亿"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="预训练数据量（GB））",
                type_="value",
                axislabel_opts=opts.LabelOpts(formatter="{value} GB"),
                offset=-100,
            )
        )
        .add_yaxis(
            series_name='Transformer层数',
            stack="总量",
            y_axis=y_data_1,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="参数量（亿）",
            stack="总量",
            y_axis=y_data_2,
            yaxis_index=1,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="预训练数据量（GB）",
            stack="总量",
            y_axis=y_data_3,
            yaxis_index=2,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_series_opts(
            opts.TextStyleOpts(font_size=16), )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="GPT参数",title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross",
                                          textstyle_opts=opts.TextStyleOpts(font_size=20)),
            yaxis_opts=opts.AxisOpts(
                name='Transformer层数',
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axislabel_opts=opts.LabelOpts(formatter="{value} 层")
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
            # 右上角贴图
            graphic_opts=[
                opts.GraphicImage(
                    graphic_item=opts.GraphicItem(
                        id_="logo", right=20, top=20, z=-10, bounding="raw", origin=[75, 75]
                    ),
                    graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                        image="ChatGPT.png",
                        width=100,
                        height=100,
                        opacity=0.4,
                    ),
                )
            ],
            # 工具箱功能是否显示
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            # 图例设置
            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=20))
        )
    )
    c = (
        Grid(init_opts=opts.InitOpts(width=width,height=height))
        .add(
            chart=c,
            grid_opts=opts.GridOpts(pos_left="5%", pos_right="4%", pos_bottom="5%"),
        )
    )

    return c

def Character(width,height):
    # 所使用的数据
    data = [
        # ChatGPT特点
        {
            "value": 40,
            "name": "ChatGPT特点",
            "children":[
             {"value": 4, "name": "敢于质疑"},
             {"value": 4, "name": "支持连续多轮对话"},
             {"value": 4, "name": "大幅度提升准确性"},
             {"value": 4, "name": "支持上下文理解"},
             {"value": 4, "name": "承认无知"},
             {"value": 4, "name": "主动承认错误"},
             {"value": 8, "name": "大幅度提升了对用户意图的理解"},]
        },
        # ChatGPT使用的技术
        {
            "value": 40,
            "name": "ChatGPT使用的技术",
            "children": [
                {"value": 40, "name": "Transformer",},
                {"value": 40, "name": "RLHP（人类反馈强化学习）", },
                {"value": 40, "name": "TAMER框架（评估式强化人工训练代理）", },
            ],
        },
        # GPT家族所使用的参数量
        {
            "value": 40,
            "name": "ChatGPT可以完成的任务",
            "children": [
                {"value": 24, "name": "协助客服"},
                {"value": 48, "name": "聊天机器人"},
                {"value": 24, "name": "自动写作"},
                {"value": 24, "name": "智能推荐"},
                {"value": 24, "name": "语音交互"},
                {"value": 24, "name": "语言翻译"},
                {"value": 24, "name": "智能搜索"},
                {"value": 24, "name": "决策支持"},
                {"value": 24, "name": "智能诊断"},
                {"value": 24, "name": "分析预测"},
                {"value": 24, "name": "数据挖掘"},
            ],
        },
    ]

    c = (
        TreeMap()
        .add(series_name="ChatGPT相关",
             leaf_depth=1,
             data=data,
             )
        .set_series_opts(
            opts.TextStyleOpts(font_size=25),)
        .set_global_opts(
            # 浮动提示框设置
            tooltip_opts=opts.TooltipOpts(is_show_content=False),
            # 标题设置
            title_opts=opts.TitleOpts(title="ChatGPT",pos_left="leafDepth",
                                    title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
            # 右上角贴图
            graphic_opts=[
                opts.GraphicImage(
                    graphic_item=opts.GraphicItem(
                        id_="logo", right=20, top=20, z=-10, bounding="raw", origin=[75, 75]
                    ),
                    graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                        image="ChatGPT.png",
                        width=100,
                        height=100,
                        opacity=0.4,
                    ),
                )
            ],
            # 工具箱功能是否显示
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            # 图例设置
            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=20))
        )
    )
    c = (
        Grid(init_opts=opts.InitOpts(width=width,height=height))
        .add(
            chart=c,
            grid_opts=opts.GridOpts(pos_left="5%", pos_right="4%", pos_bottom="5%"),
        )
    )
    return c

def BadBenifits(width,height):
    # 所使用的数据
    data = [
        # ChatGPT的优缺点
        {"value": 40,
        "name": "ChatGPT优点",
        "children":[
         {"value": 4, "name": "自然语言生成能力"},
         {"value": 4, "name": "多样性"},
         {"value": 4, "name": "上下文理解"},
         {"value": 4, "name": "可扩展性"},]
     },
    # ChatGPT缺点
    {
        "value": 40,
        "name": "ChatGPT缺点",
        "children": [
            {"value": 40, "name": "数据偏差",},
            {"value": 40, "name": "限制", },
            {"value": 40, "name": "生成的文本质量", },
            {"value": 40, "name": "安全性问题", },
            {"value": 40, "name": "计算代价", },
        ],},
    ]
    c = (
        TreeMap(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
        .add(series_name="ChatGPT优缺点",
             leaf_depth=1,
             data=data,
             )
        .set_series_opts(
            opts.TextStyleOpts(font_size=25),
        )
        .set_global_opts(
            # 浮动提示框设置
            tooltip_opts=opts.TooltipOpts(is_show_content=False),
            # 标题设置
            title_opts=opts.TitleOpts(title="ChatGPT",pos_left="leafDepth",
                                  title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
            # 右上角贴图
            graphic_opts=[
                opts.GraphicImage(
                    graphic_item=opts.GraphicItem(
                        id_="logo", right=20, top=20, z=-10, bounding="raw", origin=[75, 75]
                    ),
                    graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                        image="ChatGPT.png",
                        width=100,
                        height=100,
                        opacity=0.4,
                    ),
                )
            ],
            # 工具箱功能是否显示
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            # 图例设置
            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=20))
        )
    )
    c = (
        Grid(init_opts=opts.InitOpts(width=width,height=height))
        .add(
            chart=c,
            grid_opts=opts.GridOpts(pos_left="5%", pos_right="4%", pos_bottom="5%"),
        )
    )
    return c


tab=Tab(page_title='ChatGPT')
width="1600px"
height="900px"
tab.add(History(width,height),'ChatGPT的演化历史')
tab.add(Parameters(width,height),'GPT家族的参数演化')
tab.add(Character(width,height),'ChatGPT的功能及其特征')
tab.add(BadBenifits(width,height),'ChatGPT的优劣势')
tab.render('Visualize_ChatGPT.html')
