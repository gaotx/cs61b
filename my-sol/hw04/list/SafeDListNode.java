/* SafeDListNode.java */

package list;

public class SafeDListNode extends DListNode {
	protected DList lst;

	SafeDListNode(Object i, SafeDListNode p, SafeDListNode n, DList lst) {
		super(i, p, n);
		this.lst = lst;
	}
}