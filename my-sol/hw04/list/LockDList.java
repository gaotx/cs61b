/* LockDList.java */

package list;

public class LockDList extends DList {

	public void lockNode(DListNode node) {
		if (node instanceof LockDListNode) {
			((LockDListNode)node).locked = true;
		}
	}

	public void remove(DListNode node) {
		if (node == null && node instanceof LockDListNode && ((LockDListNode)node).locked) return;
		super.remove(node);
	}

	public static void main(String[] args) {
	    System.out.println("testing");
	    LockDList lst = new LockDList();
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
	    // next(), prev()
	    System.out.println("Testing next() of 1000 is " + lst.next(lst.head.next).item);
	    System.out.println("Testing prev() of 55.55 is " + lst.prev(lst.head.prev).item);
	    System.out.println("Testing next() of 55.55 is " + lst.next(lst.back()));
	    System.out.println("Testing prev() of 1000 is " + lst.prev(lst.front()));
	    // test insertAfter and insertBefore
	    DListNode midNode = lst.next(lst.front());
	    lst.insertBefore("hello",midNode);
	    System.out.println("Testing insertBefore of 3: "+lst);
	    lst.insertAfter("what-ever",midNode);
	    System.out.println("Testing insertAfter of 3: "+lst);
	    // test remove
	    lst.remove(lst.next(lst.front()));
	    System.out.println("Testing remove 'hello': " + lst);
	    // test remove locked node
	    lst.lockNode(lst.prev(lst.back()));
	    lst.remove(lst.prev(lst.back()));
	    System.out.println("Testing remove locked 'what-ever': " + lst);
	}
}