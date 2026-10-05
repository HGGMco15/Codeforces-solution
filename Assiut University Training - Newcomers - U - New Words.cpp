#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    string s,st="";
    cin>>s;
    for (const char& i:s){
        st+=tolower(i);
    }
    long long e=count(st.begin(),st.end(),'e');
    long long g=count(st.begin(),st.end(),'g');
    long long y=count(st.begin(),st.end(),'y');
    long long p=count(st.begin(),st.end(),'p');
    long long t=count(st.begin(),st.end(),'t');
    cout<<min({e,g,y,p,t})<<"\n";
}
