/* SafeDList.java */

package list;

public class SafeDList extends DList {

	//overridden methods
	protected DListNode newNode(Object item, DListNode prev, DListNode next) {
		return new SafeDListNode(item, (SafeDListNode)prev, (SafeDListNode)next, this);
	}

	public void insertAfter(Object item, DListNode node) {
		if (((SafeDListNode)node).lst != this) return;
		super.insertAfter(item, node);
	}

	public void insertBefore(Object item, DListNode node) {
		if (((SafeDListNode)node).lst != this) return;
		super.insertBefore(item, node);
	}

	public void remove(DListNode node) {
		if (((SafeDListNode)node).lst != this) return;
		super.remove(item, node);
	}

	public static void main(String[] args) {
		System.out.println("testing");
		SafeDList lst = new SafeDList();
		System.out.println("length :"+lst.length());
		System.out.println("is empty? "+lst.isEmpty());
		System.out.println("Testing empty: " + lst);
		lst.insertFront(3);
		System.out.println("Testing insert front "+lst);
		lst.insertBack(55.55);
		System.out.println("Testing insert back "+ lst);
		lst.insertFront(1000);
		System.out.println("Testing insert front with 1000 "+lst);
		System.out.println("Testing front() "+lst.front().item);
		System.out.println("Testing back() "+lst.back().item);

		// test insertAfter and insertBefore
		DListNode midNode = lst.next(lst.front());
		lst.insertBefore("hello",midNode);
		System.out.println("Testing insertBefore of 3: "+lst);
		lst.insertAfter("what-ever",midNode);
		System.out.println("Testing insertAfter of 3: "+lst);
		// test weakness
		SafeDList lst2 = new SafeDList();
		lst2.insertFront(101);
		lst2.insertFront(102);
		System.out.println("lst2 is " + lst2);
		lst2.insertBefore("weakness", lst.front());
		System.out.println("Testing insertBefore() of 1000 in lst using lst2");
		System.out.println("lst: " + lst + " length: " + lst.length() + "\nlst2: " + lst2 + " length: " + lst2.length());
	}
}