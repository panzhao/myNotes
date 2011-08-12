#include <stdio.h>
#include <string.h>

/*joseph circle*/
int joseph(int peop_num, int kick_num)
{
    int store_peop[peop_num];
    int i = 0;

    /*循环对函数数据进行初始化*/
    for (i = 0; i < peop_num; i++)
    {
        store_peop[i] = 0;
    }

    int mark = 0; /*用来标记数数*/
    int count = 0; /*用来计算被踢出的人的总数*/
    
    i = 0;
    
    /*循环踢出人*/
    while (count < peop_num - 1)
    {
        if (store_peop[i] == 0)
	{
	    mark++;
	}

	if (mark == kick_num)
	{
	    store_peop[i] = 1;
	    mark = 0;
	    count++;
	}
        
	i++;
	i = i % peop_num;
    }

    for (i = 0; i < peop_num; i++)
    {
        if (store_peop[i] != 1)
	{
	    printf("The last people is %d\n", i + 1);
	}
    }
}

int main()
{
    int peop_num = 1000;
    int kick_num = 15;

    joseph(peop_num, kick_num);

    return 0;
}
