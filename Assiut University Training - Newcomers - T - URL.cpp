#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    bool start=false;
    vector<string> a;
    string s,st="";
    getline(cin,s);
    for (char i:s){
        if (i=='='){
            start=true;
        }else{
            if (i!='&'){
                if (start){
                    st+=i;
                }
            }else{
                if (!st.empty()){
                    a.push_back(st);
                    st="";
                    start=false;
                }
            }
        }
    }
    if (!st.empty()){
        a.push_back(st);
        st="";
    }
    for (long long i=0;i<a.size();++i){
        if (i==0){
            cout<<"username: "<<a[i]<<"\n";
        }else if (i==1){
            cout<<"pwd: "<<a[i]<<"\n";
        }else if (i==2){
            cout<<"profile: "<<a[i]<<"\n";
        }else if (i==3){
            cout<<"role: "<<a[i]<<"\n";
        }else{
            cout<<"key: "<<a[i];
        }
    }
}
