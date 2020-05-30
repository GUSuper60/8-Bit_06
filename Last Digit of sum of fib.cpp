#include<iostream>
using namespace std;
int sumfib(int n)
{
    if(n<=1)
    {
        return 1;
    }
    return sumfib(n-1)+sumfib(n-2);
}
int main()
{
    int n;
    cin>>n;
    cout<<sumfib(n)%10;
    return 0;
}