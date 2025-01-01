#include<iostream>
using namespace std;

int main(){
   double a,b;
   char c;
   cout<<"Pilih angka pertama\t: ";
   cin>>a;
   cout<<endl;
   cout<<"Pilih operasi hitung\t: ";
   cin>>c;
  cout<<endl;
   cout<<"Pilih angka kedua\t: ";
   cin>>b;
  cout<<endl;
   if(c=='+'){
     cout<<"a + b = "<<a+b<<endl;
   }else if(c=='-'){
     cout<<"a - b = "<<a-b<<endl;
   }else if(c=='*'){
     cout<<"a x b = "<<a*b<<endl;
   }else if(c=='/'){
     cout<<"a / b = "<<a/b<<endl;
   }else{
     cout<<"[Syntax Error]" << endl;
   }
    return 0;
}
