//取球博弈
// import java.util.Scanner;
// public class Main {
// 	static int ns[] = new int[3];//可取数目
// 	static int xs[] = new int[5];//初始的球数
// 	static char dp[][][] = new char[2][1000][1000];//动态规划保存数组，保存的是玩家方，A玩家手上球数，B玩家手上球数这个局面的结果
	
// 	//求数组的最小值
// 	public static int min(int a[]) {
// 		int min=9999;
// 		for (int i : a) {
// 			if (min>i) {
// 				min=i;
// 			}
// 		}
// 		return min;
// 	}
// 	 //玩家名，A玩家手里球数，B玩家手里球数,开局球数
// 	static char dfs(int p,int Aown,int Bown,int totoalNum){
// 		int min = min(ns);//可取球数的最小值
// 		int rest = totoalNum - Aown - Bown;//当前局中场上剩余球数，总球数-A拥有球数-B拥有的球数
// 		if (dp[p][Aown][Bown] != '\u0000') {//java中char类型如果没有初始化就是\u0000 即一个空格
// 			return dp[p][Aown][Bown];//动态规划，如果已经计算过（初始化过），直接返回即可
// 		}
// 		if (rest < min) {//如果最小能取2个，而场上只有1个，则双方都不能再去，开始判输赢
// 			if (Aown % 2 == 1 && Bown % 2 == 0) {//如果A奇B偶，则赢，注意+表示的是A赢这个局面
// 				dp[p][Aown][Bown] = '+';  
// 			}
// 			else if (Aown % 2 == 0 && Bown % 2 == 1) {//A输局面
// 				dp[p][Aown][Bown] = '-';
// 			}else {
// 				dp[p][Aown][Bown] = '0';
// 			}
// 			return dp[p][Aown][Bown];
// 		}
		
// 		if (p==0) {//如果当前轮到先手A取球
// 			boolean iseq = false;//判断是否有和的可能
// 			for (int i = 0; i < ns.length; i++) {//遍历可取的球数
// 				if (rest >= ns[i]) { //如果可以取，如果最小能取2个，而场上只有1个，就不能取，ns[i] 是当前在尝试的取球数
// 					if (dfs(1, Aown + ns[i], Bown,totoalNum)=='+') {//对接下来的取球进行遍历，只要找到一个取球方法使得A赢，那么A就能赢
// 						return dp[0][Aown][Bown] = '+';
// 					}else if (dfs(1, Aown + ns[i], Bown,totoalNum) == '0') {//如果找到能和的局面，则标记能和
// 						iseq = true;
// 					}
// 				}
// 			}
// 			//for循环遍历结束，走到这里已经肯定不能赢
// 			if (iseq) //尝试和局，看是否标记能和
// 				dp[0][Aown][Bown] = '0';
// 			else 
// 				dp[0][Aown][Bown] = '-';
			
// 		}
// 		if (p==1) {//如果轮到后手B取球
// 			boolean iseq = false;
// 			for (int i = 0; i < ns.length; i++) {
// 				if (rest >= ns[i]) { //如果可以取，如果最小能取2个，而场上只有1个，就不能取，ns[i] 是当前在尝试的取球数
// 					if (dfs(0, Aown , Bown+ ns[i],totoalNum)=='-') {//只要在A的保存数组里找到一个会输的局面，那A就会输，因为采用最聪明取法
// 						return dp[1][Aown][Bown] = '-';
// 					}else if (dfs(0, Aown , Bown+ ns[i],totoalNum) == '0') {//看是否能和
// 						iseq = true;
// 					}
// 				}
// 			}
// 			//走到这里已经不能赢，看是否能和
// 			if (iseq) 
// 				dp[1][Aown][Bown] = '0';
// 			else 
// 				dp[1][Aown][Bown] = '+';
			
// 		}
// 		return dp[p][Aown][Bown];
		
// 	}
	
	
// 	public static void main(String[] args) {
// 		Scanner scanner = new Scanner(System.in);
// 		for (int i = 0; i < ns.length; i++) {
// 			ns[i] = scanner.nextInt();
// 		}
// 		for (int i = 0; i < xs.length; i++) {
// 			xs[i] = scanner.nextInt();
// 		}
// 		int k;
// 		for (int i = 0; i < xs.length; i++) {
// 			dp = new char[2][1000][1000];//每次新开一局要重新初始化dp数组
// 			k = dfs(0, 0, 0,xs[i]);
// 			System.out.print((char)k + " ");
// 		}
// 	}
// }