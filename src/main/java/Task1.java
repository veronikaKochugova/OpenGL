import com.jogamp.opengl.GL;
import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.GLCapabilities;
import com.jogamp.opengl.GLEventListener;
import com.jogamp.opengl.GLProfile;
import com.jogamp.opengl.awt.GLCanvas;

import java.awt.*;
import java.util.Arrays;

/**
 @author veronika K. on 26.09.18 */
public class Task1
	implements GLEventListener {

	private static Frame mainFrame;
	private final double DX_1 = 100.0;
	private final double DX_2 = -70.0;

	public static void main(String[] args) {
		final GLProfile glProfile = GLProfile.get(GLProfile.GL2);
		final GLCapabilities glCapabilities = new GLCapabilities(glProfile);
		final GLCanvas canvas = new GLCanvas(glCapabilities);
		final Task1 task1 = new Task1();
		canvas.addGLEventListener(task1);
		canvas.setSize(400, 400);
		mainFrame = FrameUtil.frame("Task1", Arrays.asList(canvas));
	}

	@Override
	public void init(final GLAutoDrawable drawable) {
	}

	@Override
	public void dispose(final GLAutoDrawable drawable) {
	}

	@Override
	public void display(final GLAutoDrawable drawable) {
		final CustomShape teapot = new Teapot(drawable, 0.25);
		final CustomShape sphere = new Sphere(drawable, 0.25);
		teapot.moveOnX(DX_1/mainFrame.getWidth());
		teapot.drawWire();
		sphere.moveOnX(DX_2/mainFrame.getWidth());
		sphere.drawWire();
		//
//		drawable.getGL().getGL2().glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT);
//		final CustomShape cylinder = new Cylinder(drawable, 0.25, 0.25);
//		cylinder.rotate(60, 100, 0, 0);
//		cylinder.drawWire();
//		final CustomShape tetrahedron = new Tetrahedron(drawable);
//		tetrahedron.moveOnX(- 0.4);
//		tetrahedron.rotate(45, 40, 40, 0);
//		tetrahedron.scale(0.6, 0.6, 0.6);
//		tetrahedron.drawWire();
	}

	@Override
	public void reshape(final GLAutoDrawable drawable, final int x, final int y, final int width, final int height) {
	}
}
