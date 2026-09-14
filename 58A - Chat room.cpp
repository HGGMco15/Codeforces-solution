#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    string s,st="",ans="hello";
    long long idx=0;
    cin>>s;
    vector<char> a;
    for (char i:s){
        if (i==ans[idx]){
            idx+=1;
        }
    }
    string res(a.begin(),a.end());
    if (idx==5){
        cout<<"YES"<<"\n";
    }else{
        cout<<"NO"<<"\n";
    }
}
