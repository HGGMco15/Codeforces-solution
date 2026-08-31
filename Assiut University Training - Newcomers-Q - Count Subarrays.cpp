#include <bits/stdc++.h>
using namespace std;
void solve(){
    long long cot=0,n,val;
    cin>>n;
    vector<long long> ls;
    for (int v=0;v<n;++v){
        cin>>val;
        ls.push_back(val);
    }
    for (int i=0;i<n;++i){
        for (int j=i;j<n;++j){
            vector<long long> nls,a;
            for (int k=i;k<=j;++k){
                nls.push_back(ls[k]);
                a.push_back(ls[k]);
            }
            sort(a.begin(),a.end());
            if (a==nls){
                cot+=1;
            }
        }
    }
    cout<<cot<<"\n";
}
int main() 
{
    long long t;
    cin>>t;
    for (int c=0;c<t;++c){
        solve();
    }
}
