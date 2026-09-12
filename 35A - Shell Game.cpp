#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    long long n,a,b;
    cin>>n;
    vector<long long> c;
    for (int i=0;i<3;++i){
        if (i==n-1){
            c.push_back(1);
        }else{
            c.push_back(0);
        }
    }
    while (cin>>a>>b){
        swap(c[a-1],c[b-1]);
    }
    long long ans=distance(c.begin(),find(c.begin(),c.end(),1));
    cout<<(ans+1)<<"\n";
}
