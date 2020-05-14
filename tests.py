from django.test import TestCase

# Create your tests here.
l=[1.111,2.222,3.333]
print(round(l))


def data_show(x, y, z):
    bar_width = 0.35
    index = np.arange(len(x))
    fig, ax1 = plt.subplots(figsize=(15, 9))  # 使用subplots()创建窗口

    ax1.bar(index, y, bar_width, align='center', color='c', alpha=0.8)
    for a, b in zip(index, y):
        plt.text(a - 0.05, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    #     plt.legend(loc=2) #依次右上角，左上角，左下角，右下角
    ax2 = ax1.twinx()  # 创建第二个坐标轴
    ax2.bar(index + bar_width, z, bar_width, align='center', color='red', alpha=0.8)
    for c, d in zip(index, z):
        plt.text(c + bar_width + 0.05, d + 0.05, '%.0f' % d, ha='center', va='bottom', fontsize=10)
    #     plt.legend(loc=1)
    if R_Type == "AHL":
        plt.title("{}-{}   少收行李件数前10航站".format(S_Time, E_Time))
    elif R_Type == "DPR":
        plt.title("{}-{}  破损行李件数前10航站".format(S_Time, E_Time))
    else:
        pass
    plt.xticks(index + bar_width / 2, x, size="small", rotation=30)
    ax1.set_xlabel("航站", fontsize=12)
    ax1.set_ylabel('行李件数', color="c", fontsize=12)
    ax2.set_ylabel('赔偿金额（USD)', color="red", fontsize=12)
    #     plt.gcf().autofmt_xdate()#自动适应刻度线密度，包括x轴，y轴
    #     fig.autofmt_xdate()
    #     for a,b in zip(index,y):
    #         plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
    #     for c,d in zip(index,z):
    #         plt.text(c+bar_width, d+0.05, '%.0f' % d, ha='center', va= 'bottom',fontsize=10)
    #     plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), fancybox=True, ncol=5)
    plt.grid()
    plt.savefig("C://Users/Administrator/Desktop/DPR_TOP10.png")
    plt.show()