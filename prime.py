import math

n = int(raw_input())
for i in range(2, n):
    if i == 2 or i == 3:
        print i
    if math.pow(i, 2) % 24 == 1:
        print i
    # if i % 6 == 1 or i % 6 == 5:
    #     for j in range(5, int(math.sqrt(i)), 2):
    #         if i % j == 0:
    #             return
    #     print i

    #     public void prime(int n)
    # {
    #     if(n==2||n==3)
    #     {
    #         System.out.println("Prime");
    #         return;
    #     }
    #     if(n%6==1||n%6==5)
    #     {
    #         for(int i=5;i<Math.sqrt(n);i=i+2)
    #         {
    #             if(n%i==0)
    #             {
    #                 System.out.println("Not Prime");
    #                 return;
    #             }
    #         }
    #         System.out.println("Prime");
    #         return;
    #     }
    #    System.out.println("Not Prime");
    # }
