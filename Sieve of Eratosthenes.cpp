#include<iostream>
using namespace std;
void solution(int *arr,int n)
{
    long int i,j;
    for(i=3;i<=n;i+=2)
    {
        arr[i]=1;
    }
    for(i=3;i<n;i++)
    {
        for(j=i*i;j<n;j+=i)
        {
            arr[j]=0;
        }
    }
    arr[2]=1;
    arr[0]=arr[1]=0;
}
int main()
{
    int n,arr[1000000]={0};
    cin>>n;
    solution(arr,n);
    for(int i=0;i<n;i++)
    {
        if(arr[i]==1)
        {
            cout<<i<<" ";
        }
    }
    return 0;
}