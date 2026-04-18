import java.util.Scanner;
public class Main {
	static int list[]={//存放后缀序列，这样插和删除很容易
		0,0,0,0,0,//注cccbba=1,2,3,0,……
		0,0,0,0,0,
		0,0,0,0,0,
		0,0,0,0,0,
		0,0,0,0,0,
		0
	};
	static int[] str=new int[300];//存放前缀序列
	static void reset() {//后缀序列清零
		int i=0;
		while(i<26&&list[i]!=0) {
			list[i]=0;
			++i;
		}
	}
	static int getrnum() {//计算逆序数（分三步）
		int cnt=0;
		for(int i=0;str[i]!=0;++i) {//前缀的逆序数
			for(int j=i;str[j]!=0;++j) {
				if(str[i]>str[j]) {
					++cnt;
				}
			}
		}
		for(int i=0;str[i]!=0;++i) {//前缀对后缀的逆序数
			for(int j=25;j>=0;--j) {
				if(str[i]-'a'>j) {
					cnt+=list[j];
				}
			}
		}
		int temp=0;
		for(int i=0;i<26;++i) {//后缀的逆序数
			cnt+=temp*list[i];
			temp+=list[i];
		}
		return cnt;
	}
	static int getinc(int c) {//获得最大逆序增量（特殊步骤中代替求逆序数函数用来提速）（可以认为在数字符串里有多少非c(传入的参数)字符）(也就是插入c逆序数能增加多少)
		int i=0,cnt=0;
		while(str[i]!=0) {
			if(str[i]>(c+'a')) {
				cnt++;
			}
			++i;
		}
		for(i=0;i<26;++i) {
			if(i!=c) {
				cnt+=list[i];
			}
		}
		return cnt;
	}
	static void set() {//在后部序列中插入元素，保证逆序数最大
		int max=0,temp=0,index=0;
		for(int i=0;i<26;++i) {
			list[i]++;
			if((temp=getinc(i))>max) {//找出使逆序数增得最快的字符插入（这里比用增而直接记录逆序数不影响结果，但慢一些，数据10000左右要5秒左右，会超时的，不然我也不会编这么个对于的函数。。）
				index=i;
				max=temp;
			}
			list[i]--;
		}
		list[index]++;
	}
	static void getMaxStr(int l) {//获取前缀确定且长度确定的前提下的最大逆序数字串
		reset();
		for(int i=0;str[i]!=0;++i,--l);
		while(l>0) {
			set();
			--l;
		}
	}
	static void printstr() {//打印目标字符串
		String Str="";
		int i=0;
		while(str[i]!=0) {
			Str+=(char)str[i];
			++i;
		}
		for(i=25;i>=0;--i) {//这里其实没用，既然不执行也不会影响效率，留着吧，后缀最后是空的，但曾经存在过。。。
			for(int j=0;j<list[i];++j) {
				Str+=(char)(i+'a');
			}
		}
		System.out.println(Str);
	}
	static void getans(int num,int l) {//l是字串长度
		for(int i=0;i<l;++i) {
			for(int j=0;j<26;++j) {//每个位从a开始试
				str[i]=j+'a';
				getMaxStr(l);//获取指定前缀最大逆字串
				if(getrnum()>=num) {//超了就下一个
					break;
				}
			}
		}
	}
	public static void main(String[] args){//这了很简洁了
		int num;
		Scanner sc = new Scanner(System.in);
		num=sc.nextInt();//获取输入
		sc.close();
		int l=0;
		while(getrnum()<num) {//获取最短字串长
			++l;
			getMaxStr(l);
		}
		getans(num,l);//获得目标字串
		printstr();//打印
	}
}
