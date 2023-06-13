import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 创建标题
st.title('Gallery')

# 在侧边栏中创建一个选择框来选择结果展示页面
page = st.sidebar.selectbox('Choose a page', ['Explanations', 'Other Result Page'])

if page == 'Explanations':
    # 创建一个选择框来选择系统
    system = st.selectbox('Choose a system to see explanations', ['Mimicus', 'DAMD', 'VulDeePecker'])

    if st.button('Load'):
        # 当用户点击'Load'按钮时执行
        if system == 'Mimicus':
            st.header('Mimicus')
            # 特征名称
            IG = [1,0.75721291,0.59776144,0.52017018,0.37380879,0.3975868,0.37120876,0.27216313,0.24244715,-0.24116577]
            Gradient = [1,0.77165814,0.60648558,0.51769901,0.39355636,0.38596884,0.37118986,0.26948801,0.24126262,0.2378897]
            LIME = [0.55479926,0.53199047,0.52494689,-0.60058626,-0.72711186,0.56302063,-0.65642783,-0.70010357,-0.62646985,-1]
            LEMNA = [0.66072644,0.79990058,0.79867024,0.66329716,1,0.75803258,0.90570064,-0.77596588,0.90381712,-0.63274222]

            lenth=10
            # 设置柱形的宽度
            bar_width = 0.15
            # 创建柱状图
            plt.bar(np.arange(lenth) - bar_width, IG, width=bar_width, label='IG')
            plt.bar(np.arange(lenth), Gradient, width=bar_width, label='Gradient')
            plt.bar(np.arange(lenth) + bar_width, LIME, width=bar_width, label='LIME')
            plt.bar(np.arange(lenth) + 2*bar_width, LEMNA, width=bar_width, label='LEMNA')

            plt.axhline(y=0, color='black', linewidth=1)

            # 添加标题和轴标签
            plt.title('Comparison of Feature Importance-Benign 1')
            plt.xlabel('Features')
            plt.ylabel('Depth')

            # 调整横坐标标签的显示角度
            plt.xticks(np.arange(lenth), np.arange(1, lenth+1))
            # 自动调整子图布局
            plt.tight_layout()

            # 添加图例
            plt.legend()

            # 显示图形
            st.pyplot(plt.gcf())
            plt.cla()
            IG = [1.0, 0.72811858, 0.60883541, 0.53117895, 0.45866689, 0.35404817, -0.3459963, -0.38474751, -0.46588383, -0.59088229]
            Gradient =  [1.0, 0.70544267, 0.59025025, 0.5124709, 0.47581458, 0.34251946, -0.3238798, -0.3482982, -0.45472067, -0.59009271]
            LIME =  [0.56920146, 0.34559717, 0.47492166, 0.07449177, 0.20279706, 0.41185314, -0.04930782, -0.10226361, -1.0, -0.62832953]
            LEMNA =  [0.4261722, 0.39735195, 0.52690128, 0.60967298, -0.05485781, 0.95883105, -0.46635915, 0.33824764, -0.7907793, -0.07559517]
            
            lenth=10
            # 设置柱形的宽度
            bar_width = 0.15
            # 创建柱状图
            plt.bar(np.arange(lenth) - bar_width, IG, width=bar_width, label='IG')
            plt.bar(np.arange(lenth), Gradient, width=bar_width, label='Gradient')
            plt.bar(np.arange(lenth) + bar_width, LIME, width=bar_width, label='LIME')
            plt.bar(np.arange(lenth) + 2*bar_width, LEMNA, width=bar_width, label='LEMNA')

            plt.axhline(y=0, color='black', linewidth=1)

            # 添加标题和轴标签
            plt.title('Comparison of Feature Importance-Benign 2')
            plt.xlabel('Features')
            plt.ylabel('Depth')

            # 调整横坐标标签的显示角度
            plt.xticks(np.arange(lenth), np.arange(1, lenth+1))
            # 自动调整子图布局
            plt.tight_layout()

            # 添加图例
            plt.legend()

            # 显示图形
            st.pyplot(plt.gcf())
            plt.cla()
            plt.bar(np.arange(lenth) - bar_width, IG, width=bar_width, label='IG')
            plt.bar(np.arange(lenth), Gradient, width=bar_width, label='Gradient')
            plt.bar(np.arange(lenth) + bar_width, LIME, width=bar_width, label='LIME')
            plt.bar(np.arange(lenth) + 2*bar_width, LEMNA, width=bar_width, label='LEMNA')

            plt.axhline(y=0, color='black', linewidth=1)

            # 添加标题和轴标签
            plt.title('Comparison of Feature Importance-Malicious 1')
            plt.xlabel('Features')
            plt.ylabel('Depth')

            # 调整横坐标标签的显示角度
            plt.xticks(np.arange(lenth), np.arange(1, lenth+1))
            # 自动调整子图布局
            plt.tight_layout()

            # 添加图例
            plt.legend()

            # 显示图形
            st.pyplot(plt.gcf())
            plt.cla()
            IG = [1.0, 0.67214071, 0.42704697, 0.40684834, 0.35707843, 0.28818617, 0.2500375, 0.21785379, -0.28323633, -0.62872802]
            Gradient =  [1.0, 0.6777789, 0.42945053, 0.41336017, 0.37069038, 0.29701948, 0.24958918, 0.22769294, -0.29721905, -0.63413497]
            LIME =  [1.0, 0.68029226, 0.6772547, 0.55166205, 0.40624905, 0.43678641, 0.42822345, -0.76916744, -0.52523498, -0.99882429]
            LEMNA =  [1.0, 0.73139742, 0.46939839, 0.5801568, 0.4846231, 0.48640017, 0.53658801, 0.49026934, -0.6452203, -0.65008755]
            
            bar_width = 0.15
            # 创建柱状图
            plt.bar(np.arange(lenth) - bar_width, IG, width=bar_width, label='IG')
            plt.bar(np.arange(lenth), Gradient, width=bar_width, label='Gradient')
            plt.bar(np.arange(lenth) + bar_width, LIME, width=bar_width, label='LIME')
            plt.bar(np.arange(lenth) + 2*bar_width, LEMNA, width=bar_width, label='LEMNA')

            plt.axhline(y=0, color='black', linewidth=1)

            # 添加标题和轴标签
            plt.title('Comparison of Feature Importance-Malicious 2')
            plt.xlabel('Features')
            plt.ylabel('Depth')

            # 调整横坐标标签的显示角度
            plt.xticks(np.arange(lenth), np.arange(1, lenth+1))
            # 自动调整子图布局
            plt.tight_layout()

            # 添加图例
            plt.legend()

            # 显示图形
            st.pyplot(plt.gcf())
            plt.cla()
        elif system == 'DAMD':
            st.header('DAMD')
            IG = [-0.020153602169881494, 0.3122217600431931, 0.15908539394542529, 0.12051039468538449, 0.05962470283749583, -0.0205150932449325, -0.02079717494790633, -0.06040613940241074, -0.11925722304798995, 0.1199566902507345]  
            Gradient =  [0.6614875407725817, 0.22956849703900248, -0.06018379456455294, 0.9971684419213891, 0.19808717726827849, 0.0396620253920336, -0.0706592588298824, 0.29054609566781736, 0.06967308401904851, -0.29105286343630776]
            LIME =  [0.0007871351695524126, -0.0016973212755189379, -0.0010362698201807263, 0.0009192529860455836, -0.0018197474754395467, -0.0007802687736020969, -0.0017925558009864399, 0.0014514770447221846, 0.0009513723853788339, -0.0007164170422323813]
            LEMNA =  [0.6709830339078221, 0.9679029258096842, 0.9606810770498841, 0.6909952743978196, 0.5198990846804713, 0.940789430657129, 0.9879391663778003, 0.958579959167976, 0.9606132203184121, 0.990257260763873]


            # 特征名称
            lenth=10


            # 设置柱形的宽度
            bar_width = 0.15
            print(lenth)
            # 创建柱状图
            plt.bar(np.arange(lenth) - bar_width, IG, width=bar_width, label='IG')
            plt.bar(np.arange(lenth), Gradient, width=bar_width, label='Gradient')
            plt.bar(np.arange(lenth) + bar_width, LIME, width=bar_width, label='LIME')
            plt.bar(np.arange(lenth) + 2*bar_width, LEMNA, width=bar_width, label='LEMNA')

            plt.axhline(y=0, color='black', linewidth=1)

            # 添加标题和轴标签
            plt.title('Comparison of Feature Importance-Benign 1')
            plt.xlabel('Features')
            plt.ylabel('Depth')

            plt.ylim(0, 1)
            # 调整横坐标标签的显示角度
            plt.xticks(np.arange(lenth), np.arange(1, lenth+1))
            # 自动调整子图布局
            plt.tight_layout()

            # 添加图例
            plt.legend()

            # 显示图形
            st.pyplot(plt.gcf())
            plt.cla()
            IG = [0.0004663610247526652, 0.020690210663257533, -0.539458162941635, 0.4400944352534282, 0.42907009538865104, 0.030043554169168988, -0.24794213777485188, 0.1313837506393435, 0.7603510700907402, 0.9996910848418108]
            Gradient =  [0.18985199038931003, -0.028006583461126437, -0.07102541753373191, 0.04145331092998404, 0.06886706296467413, 0.13977414071994995, -0.0010613123986615504, 1.0013404827950747, 0.6886740591403181, 0.09990573444335789]
            LIME =  [0.0013471582658105014, -0.0011109032797306437, -4.9264151205141386e-05, 5.0349513299629975e-05, 0.0015247278634423363, -0.0019317002608918957, -0.00021235133745493536, 0.000683783086948371, -0.00023990967409810775, 0.00033297613591835867]
            LEMNA =  [0.6103076201262166, 0.5999013363316805, 0.989387888541787, 0.6091369662664762, 0.6296864132809135, 1.0010113209195628, 0.9904983205776808, 0.6809845432031973, 0.7215036257904814, 0.7012726236643775]
            
            lenth=10

            # 设置柱形的宽度
            bar_width = 0.15
            print(lenth)
            # 创建柱状图
            plt.bar(np.arange(lenth) - bar_width, IG, width=bar_width, label='IG')
            plt.bar(np.arange(lenth), Gradient, width=bar_width, label='Gradient')
            plt.bar(np.arange(lenth) + bar_width, LIME, width=bar_width, label='LIME')
            plt.bar(np.arange(lenth) + 2*bar_width, LEMNA, width=bar_width, label='LEMNA')

            plt.axhline(y=0, color='black', linewidth=1)

            # 添加标题和轴标签
            plt.title('Comparison of Feature Importance-Benign 2')
            plt.xlabel('Features')
            plt.ylabel('Depth')


            # 调整横坐标标签的显示角度
            plt.xticks(np.arange(lenth), np.arange(1, lenth+1))
            # 自动调整子图布局
            plt.tight_layout()

            # 添加图例
            plt.legend()

            # 显示图形
            st.pyplot(plt.gcf())
            plt.cla()
            IG = [0.010280881390369069, 0.011721346405922518, -0.0011793034333007224, -0.048655251617103365, 0.019104015100867504, -0.04978770031963124, 0.0018087291200568503, -0.6984088230060558, 0.0009729638251069263, -1.0006752725579267]
            Gradient =  [0.06936156630112414, -0.00962277502826259, 0.0010666259900229222, 0.02908207883047143, -0.17997932677491718, -0.5091262779830017, 0.002809471580624735, 0.1478573248285099, 0.06937517997883615, 0.37914736687291856]
            LIME =  [-0.7098730370703134, 0.1295760549595098, 0.1189409961618143, -0.34909874444992034, 0.07165680703576485, 0.40957473836484964, 0.4106446766584914, -0.24988109410970116, -0.24963960518902936, 0.37921571984064234]
            LEMNA =  [-0.1903740143518438, -0.18912100885250574, -0.2797976468768531, 0.008259733905529596, -0.11877784937718905, -0.1910937118759105, -0.32794703709203005, -0.12994656445847164, -0.19930042794585362, -0.1501228609079787]

            lenth=10

            # 设置柱形的宽度
            bar_width = 0.15
            print(lenth)
            # 创建柱状图
            plt.bar(np.arange(lenth) - bar_width, IG, width=bar_width, label='IG')
            plt.bar(np.arange(lenth), Gradient, width=bar_width, label='Gradient')
            plt.bar(np.arange(lenth) + bar_width, LIME, width=bar_width, label='LIME')
            plt.bar(np.arange(lenth) + 2*bar_width, LEMNA, width=bar_width, label='LEMNA')

            plt.axhline(y=0, color='black', linewidth=1)

            # 添加标题和轴标签
            plt.title('Comparison of Feature Importance-Benign 3')
            plt.xlabel('Features')
            plt.ylabel('Depth')


            # 调整横坐标标签的显示角度
            plt.xticks(np.arange(lenth), np.arange(1, lenth+1))
            # 自动调整子图布局
            plt.tight_layout()

            # 添加图例
            plt.legend()

            # 显示图形
            st.pyplot(plt.gcf())
            plt.cla()

            IG = [-0.030490020191821454, -1.082780890751872e-05, -0.07141079423802695, 0.16835528750520923, -0.7812078021780204, 0.16017003357677692, 0.4387872045859873, 0.02088545768604085, -0.49977574667063196, -0.4510640760367647]
            Gradient =  [0.14046970389028088, -0.0007725103662246463, 0.01898191518997941, 0.16907953689317856, -0.8597160926956149, -0.4073702185818332, -0.03888232787365626, -0.029172258324294868, -0.12126619311192016, -0.999288018636114]
            LIME =  [-0.3498660766507666, 0.16063325533670625, 0.3108064979767586, 1.000764250512486, 0.0005590522528908014, 0.5096464411305588, 0.6187700745818511, 0.5293371221327033, 0.10002128814531679, -0.1208882218863047]      
            LEMNA =  [0.9985172838028948, 0.9994627650399873, 0.061178116502258774, -0.04164678906061806, -0.07987328939716644, -0.010115790161103309, 0.6898879892596443, -0.11979446775258491, -0.5490735540492343, 0.2386128258278831]
            
            lenth=10

            # 设置柱形的宽度
            bar_width = 0.15
            print(lenth)
            # 创建柱状图
            plt.bar(np.arange(lenth) - bar_width, IG, width=bar_width, label='IG')
            plt.bar(np.arange(lenth), Gradient, width=bar_width, label='Gradient')
            plt.bar(np.arange(lenth) + bar_width, LIME, width=bar_width, label='LIME')
            plt.bar(np.arange(lenth) + 2*bar_width, LEMNA, width=bar_width, label='LEMNA')

            plt.axhline(y=0, color='black', linewidth=1)

            # 添加标题和轴标签
            plt.title('Comparison of Feature Importance-Malicious 1')
            plt.xlabel('Features')
            plt.ylabel('Depth')


            # 调整横坐标标签的显示角度
            plt.xticks(np.arange(lenth), np.arange(1, lenth+1))
            # 自动调整子图布局
            plt.tight_layout()

            # 添加图例
            plt.legend()

            # 显示图形
            st.pyplot(plt.gcf())
            plt.cla()
        elif system == 'VulDeePecker':
            st.header('VulDeePecker')
            IG = [-0.09,-0.05,-0.12,-0.15,-0.1,-0.08,-0.18,0.02,-0.09,-0.07]
            Gradient = [0.01 ,-0.06 ,0.02 ,0.04 ,0.05 ,0.14 ,0.8 , -0.48, 0.01, -0.13]
            LIME = [-0.51,0.39,0.32,-0.2,-0.07,0.48,-0.26,0.49,0.51,0.31]
            LEMNA = [0.57,0.58,0.58,0.59,0.61,0.62,0.88,0.98,0.57,0.99]
            lenth=10

            # 设置柱形的宽度
            bar_width = 0.15
            print(lenth)
            # 创建柱状图
            plt.bar(np.arange(lenth) - bar_width, IG, width=bar_width, label='IG')
            plt.bar(np.arange(lenth), Gradient, width=bar_width, label='Gradient')
            plt.bar(np.arange(lenth) + bar_width, LIME, width=bar_width, label='LIME')
            plt.bar(np.arange(lenth) + 2*bar_width, LEMNA, width=bar_width, label='LEMNA')

            plt.axhline(y=0, color='black', linewidth=1)

            # 添加标题和轴标签
            plt.title('Comparison of Feature Importance-Not vulnerable 1')
            plt.xlabel('Features')
            plt.ylabel('Depth')


            # 调整横坐标标签的显示角度
            plt.xticks(np.arange(lenth), np.arange(1, lenth+1))
            # 自动调整子图布局
            plt.tight_layout()

            # 添加图例
            plt.legend()

            # 显示图形
            st.pyplot(plt.gcf())
            plt.cla()
            
            
            IG = [0.23, 0.18, -0.04, 0.02, 0.06, 0.23, 0.18, -0.04, 0.02, -0.04]
            Gradient = [0.29, -0.01, 0.27, -0.12, -0.13, 0.29, -0.01, 0.27, -0.12, 0.07]
            LIME = [-0.15, -0.18, 0.23, 0.18, 0.36, -0.15, 0.18, 0.23, 0.18, -0.57]
            LEMNA = [0.43, 0.69, 0.71, 0.93, 0.94, 0.43, 0.69, 0.71, 0.93, 0.95]
            
            lenth=10

            # 设置柱形的宽度
            bar_width = 0.15
            print(lenth)
            # 创建柱状图
            plt.bar(np.arange(lenth) - bar_width, IG, width=bar_width, label='IG')
            plt.bar(np.arange(lenth), Gradient, width=bar_width, label='Gradient')
            plt.bar(np.arange(lenth) + bar_width, LIME, width=bar_width, label='LIME')
            plt.bar(np.arange(lenth) + 2*bar_width, LEMNA, width=bar_width, label='LEMNA')

            plt.axhline(y=0, color='black', linewidth=1)

            # 添加标题和轴标签
            plt.title('Comparison of Feature Importance-Not vulnerable 2')
            plt.xlabel('Features')
            plt.ylabel('Depth')


            # 调整横坐标标签的显示角度
            plt.xticks(np.arange(lenth), np.arange(1, lenth+1))
            # 自动调整子图布局
            plt.tight_layout()

            # 添加图例
            plt.legend()

            # 显示图形
            st.pyplot(plt.gcf())
            plt.cla()
            IG = [1, 0.2, 0.11, 0.55, -0.03, 0.25, 0.01, -0.08, 0.48, 0.34]
            Gradient = [-0.01, 0.32, -0.08, 0.07, 0.01, -0.02, 0.55, -0.19, -0.04, 0.77]
            LIME = [0.39, 0.46, 0.17, -0.09, 0.03, 0.12, 0.07, -0.16, -0.1, 0.1]
            LENMA = [0.99, 0.96, 0.36, -0.04, -0.03, 0.37, 0.98, 0.98, 0.39, 0.99]
            
            lenth=10

            # 设置柱形的宽度
            bar_width = 0.15
            print(lenth)
            # 创建柱状图
            plt.bar(np.arange(lenth) - bar_width, IG, width=bar_width, label='IG')
            plt.bar(np.arange(lenth), Gradient, width=bar_width, label='Gradient')
            plt.bar(np.arange(lenth) + bar_width, LIME, width=bar_width, label='LIME')
            plt.bar(np.arange(lenth) + 2*bar_width, LEMNA, width=bar_width, label='LEMNA')

            plt.axhline(y=0, color='black', linewidth=1)

            # 添加标题和轴标签
            plt.title('Comparison of Feature Importance-Vulnerable')
            plt.xlabel('Features')
            plt.ylabel('Depth')


            # 调整横坐标标签的显示角度
            plt.xticks(np.arange(lenth), np.arange(1, lenth+1))
            # 自动调整子图布局
            plt.tight_layout()

            # 添加图例
            plt.legend()

            # 显示图形
            st.pyplot(plt.gcf())
            plt.cla()

elif page == 'Other Result Page':
    # 显示其他结果展示页面的内容
    st.header('Other Result Page')
    # 你的其他结果展示页面的代码...
# 创建一个标题和一个列表
st.header('Notes')
st.text('库中包含了我们文章中提到的三种深度学习安全系统的解析 ')
st.text('Mimucus:此系统使用了MLP架构，被设计用于检测恶意的PDF文档')
st.text('DAMD:此系统使用CNN处理Dalvik字节码来识别恶意的安卓应用程序。')
st.text('VulDeePecker:此系统使用RNN来发现源代码中的漏洞。')
st.text('选中对应库后，将呈现LIME, LENMA, IG和Gradient解析的结果对比图像。')
st.text('每个图象选择了10个权重较大的特征来做对比')
