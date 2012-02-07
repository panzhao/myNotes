#c++笔记
##关于c++中类的const,static const,static成员关系
    const成员必须再够找函数初始化列表中进行初始化;
    static成员在类的定义中定义，只能再类的定义体外初始化;
    const static成员必须再类的定义体之内进行定义并初始化;
