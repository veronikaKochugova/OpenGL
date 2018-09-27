import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.List;

/**
 @author veronika K. on 26.09.18 */
public class FrameUtil {

	public static Frame frame(final String name, final List<Component> items) {
		final Frame frame = new Frame(name);
		frame.setSize(800, 800);
		frame.setLocation(550, 200);
		items.forEach(i -> frame.add(i));
		frame.setVisible(true);
		frame.addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(final WindowEvent windowEvent) {
				System.exit(0);
			}
		});
		return frame;
	}
}
