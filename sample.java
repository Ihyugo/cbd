public class sample{
	public static void main(String[] args){
		int i;
		double sum,total=0.0;
		for(i=0; i<100000000; i++){
			sum = 2*i + 1;
			if(i%2 == 0)	total += 1/sum;
			else	total -= 1/sum;
		}
		System.out.println(4*total);
	}
}
