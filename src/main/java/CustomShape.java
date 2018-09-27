import com.jogamp.opengl.GL2;
import com.jogamp.opengl.GLAutoDrawable;

/**
 @author veronika K. on 27.09.18 */
abstract class CustomShape {

	protected GL2 gl;

	public CustomShape(final GLAutoDrawable drawable) {
		this.gl = drawable.getGL().getGL2();
		gl.glLoadIdentity();
	}

	abstract void drawSolid();

	abstract void drawWire();

	public void moveOnX(final double dx) {
		System.out.println(this.getClass().getSimpleName() + " moved onX " + dx);
		gl.glTranslated(dx, 0, 0);
	}

	public void moveOnY(final double dy) {
		System.out.println(this.getClass().getSimpleName() + " moved onY " + dy);
		gl.glTranslated(0, dy, 0);
	}

	public void scale(final double x, final double y, final double z) {
		gl.glScaled(x, y, z);
	}

	public void rotate(final double angle, final double x, final double y, final double z) {
		gl.glRotated(angle, x, y, z);
	}
}
