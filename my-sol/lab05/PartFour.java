/* com.gaotx.PartFour */


class SuperClass {
	public void method(int i) {
		System.out.println("SuperClass method!");
	}
}

class SubClass extends SuperClass {
	public void method(int i) {
		System.out.println("Overrided SubClass method!");
	}
}

class PartFour {
	public static void main(String[] args) {
		SubClass subVariable = new SubClass();
		((SuperClass) subVariable).method(0);//call subclass method, even cast
		
		SuperClass superVariable = new SuperClass();
		//((SubClass) superVariable).method(0);//Run-time error: super cannot be cast to sub

		SuperClass hybrid = new SubClass();//type: super; class: sub
		((SuperClass) hybrid).method(0);//call subclass method
	}
}