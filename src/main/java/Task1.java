import com.jogamp.opengl.GL;
import com.jogamp.opengl.GL2;
import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.GLCapabilities;
import com.jogamp.opengl.GLEventListener;
import com.jogamp.opengl.GLProfile;
import com.jogamp.opengl.awt.GLCanvas;
import com.jogamp.opengl.util.gl2.GLUT;

import java.awt.*;
import java.util.Arrays;

/**
 @author veronika K. on 26.09.18 */
public class Task1 implements GLEventListener {

	final private GLUT glut = new GLUT();

	public static void main(String[] args) {
		final GLProfile glProfile = GLProfile.get(GLProfile.GL2);
		final GLCapabilities glCapabilities = new GLCapabilities(glProfile);
		final GLCanvas canvas = new GLCanvas(glCapabilities);
		final Task1 task1 = new Task1();
		canvas.addGLEventListener(task1);
		canvas.setSize(400, 400);

		final Frame frame = FrameUtil.frame("Task1", Arrays.asList(canvas));
	}

	@Override
	public void init(final GLAutoDrawable drawable) {
	}

	@Override
	public void dispose(final GLAutoDrawable drawable) {
	}

	@Override
	public void display(final GLAutoDrawable drawable) {
		final GL2 gl = drawable.getGL().getGL2();
		gl.glClearColor(0,0,0,0);
		gl.glClear( GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT );

		gl.glMatrixMode(GL2.GL_PROJECTION);  // TODO: Set up a better projection?
		gl.glLoadIdentity();
		gl.gl
		gl.glOrtho(-1,1,-1,1,-2,2);
		gl.glMatrixMode(GL2.GL_MODELVIEW);

		gl.glLoadIdentity();

		// TODO: add drawing code!!  As an example, draw a GLUT teapot
		glut.glutWireTeapot(0.25);
		//glut.glutWireCube(50.0f);
		//glut.glutWireSphere(100,10,1);
	}

	@Override
	public void reshape(final GLAutoDrawable drawable, final int x, final int y, final int width, final int height) {
	}
}
