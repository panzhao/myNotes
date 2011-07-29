#include <stdio.h>

int main()
{
    char source[128] = "    bei     jing               huan ying nin!    ";
    int argc = 0;
    char *argv[16];
    char *str = source;
    
    int i = 0;
    
    while (*str != '\0')
    {
	if (*str == ' ')
	{  
	 
	   while (*str == ' ')
	   {
	       str++;
	   }
           
	   if(*str == '\0')
	   {
	       break;
	   }

	   argc++;
       
	   *--str = '\0';
          
	   argv[i++] = ++str;

	   continue;
	}

	str++;
    }

   printf("argc is %d\n", argc);

   for (i = 0; i < argc; i++)
   {
       printf("argv[%d] is: %s\n", i, argv[i]);
   }

   return 0;
}
