import java.io.Serializable;

public abstract class Token implements TokenConstants, Serializable {
	private static final long serialVersionUID = 862935679966383302L;
	public int type;
	public String file;
	
	protected boolean marked;
	protected boolean basecode = false;
	protected int hash = -1;// hash-value. set and used by main algorithm (GSTiling)
	
	public Token(int type, String file, int line) {
		this(type, file, line, -1, -1);
	}
	
	public Token(int type, String file, int line, int column, int length) {
		this.type = type;
		this.file = file;
		setLine(line>0 ? line : 1);
		setColumn(column);
		setLength(length);
	}
	
	// abstract members
	public abstract int getLine();
	public abstract int getColumn();
	public abstract int getLength();
	protected void setLine(int line) {}
	protected void setColumn(int line) {}
	protected void setLength(int line) {}
	
	// this is made to distinguish the character module.
	// maybe other modules can use it too?
	protected int getIndex() { return -1; }
	
	public static String type2string(int type) {
		return "<abstract>";
	}
	
	public String toString() {
		return type2string(type);
	}
	
	public static int numberOfTokens() { 
		return 1;
	} 
}
