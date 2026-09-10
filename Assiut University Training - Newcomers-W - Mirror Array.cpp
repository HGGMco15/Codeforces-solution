#include <bits/stdc++.h>
using namespace std;
 
int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n,m,val;
    cin>>n>>m;
    for (int i=0;i<n;++i){
        vector<long long> a;
        for (int j=0;j<m;++j){
            cin>>val;
            a.push_back(val);
        }
        for (int j=a.size()-1;j>=0;--j){
            cout<<a[j]<<" ";
        }
        cout<<"\n";
    }
}
