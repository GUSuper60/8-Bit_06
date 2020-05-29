#include<iostream>
using namespace std;
int fib(long int n)
{
    long int a=0,b=1,c=0,i;
    if(n==0 || n==1)
    {
        return n;
    }
    for(i=2;i<=n;i++)
    {
        c=(a+b)%10;
        a=b;
        b=c;
    }
    return c;
}
int main()
{
    long int n;
    cin>>n;
    cout<<fib(n+2)-fib(2);
    return 0;
}
