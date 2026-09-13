#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    map<string,long long> a;
    long long n;
    string val;
    cin>>n;
    for (long long i=0;i<n;++i){
        cin>>val;
        a[val]+=1;
    }
    auto [nm,vl]=*max_element(a.begin(),a.end(),[](auto a,auto b){return a.second<b.second;});
    cout<<nm<<"\n";
}
