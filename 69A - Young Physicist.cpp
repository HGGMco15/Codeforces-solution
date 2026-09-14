#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n,x=0,y=0,z=0,vl1,vl2,vl3;
    cin>>n;
    for (long long i=0;i<n;++i){
        cin>>vl1>>vl2>>vl3;
        x+=vl1;y+=vl2;z+=vl3;
    }
    if (x==0 && y==0 && z==0){
        cout<<"YES"<<"\n";
    }else{
        cout<<"NO"<<"\n";
    }
}
