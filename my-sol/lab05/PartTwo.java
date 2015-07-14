/* PartTwo.java */

interface Printable {
	// public void printMethod(int i);//implicit use abstract keyword, so no implementation
	// public int printMethod(int i);//compile-time error; need override in SubClass
	// public void printMethod(String i);//compile-time error; need override in SubClass
	// public void printMethod(int ii); //works
}

class SuperClass {
	public void printMethod(int i) {
		System.out.println("SuperClass's printMethod()!");
	}
}

class SubClass extends SuperClass implements Printable {
	//public void printMethod(int i) {
	//	System.out.println("SubClass's override printMethod()!");
	//}
}

public class PartTwo {
	public static void main(String[] args) {
		SubClass obj = new SubClass();
		obj.printMethod(0);
		System.out.println("Pass!");
	}
}