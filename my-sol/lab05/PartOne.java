/* PartOne.java */

class X {
	protected String str;
}

class Y extends X {

}

class PartOne {
	public static void main(String[] args) {
		X[] xa;
		Y[] ya;

		xa = new X[1];
		ya = new Y[1];

		//assign xa to ya, if xa's dynamic class is X's
		// ya = xa; // Compile-time ERROR
		// ya = (Y[]) xa; // Run-time ERROR
		xa = ya;

		//if ya references dynamic class of Y's
		xa = ya;
		ya = (Y[]) xa;// need a cast

		//assign xa to ya, if xa's dynamic class is Y's
		xa = new Y[1];
		ya = (Y[]) xa; // need a cast
		
		System.out.println("Pass!");


	}
}