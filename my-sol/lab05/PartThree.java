/* PartThree.java */

interface Instance {
	public static final int i = 0;
}

class SuperClass {
	public static final int i = 1;//value doesn't matter
}

class SubClass extends SuperClass implements Instance {
	public static void main(String[] args) {
		// System.out.print(i);//ambiguous
		System.out.println("SuperClass i is " + SuperClass.i + " using SuperClass.i");
		System.out.println("Instance i is " + Instance.i + " using Instance.i");
	}

}

