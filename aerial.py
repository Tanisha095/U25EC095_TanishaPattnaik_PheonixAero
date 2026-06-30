import cv2
image= cv2.imread(r'D:\vscode\MYCODE\pheonix\aerial.png') # Load image
if image is None:
    print("Error: Image not found")
    exit()
image = cv2.resize(image, (640, 640)) # Resize 
display = image.copy()   # Copy for drawing

rows, cols = 8, 8
h, w, _ = image.shape

cell_h = h // rows
cell_w = w // cols

selected_cell = None

def draw_grid(img):   
    for i in range(1, rows):
        cv2.line(img, (0, i * cell_h), (w, i * cell_h), (0, 255, 0), 1)
    for j in range(1, cols):
        cv2.line(img, (j * cell_w, 0), (j * cell_w, h), (0, 255, 0), 1)

def mouse_click(event, x, y, flags, param):
    global selected_cell, display

    if event == cv2.EVENT_LBUTTONDOWN:
        col = x // cell_w
        row = y // cell_h

        selected_cell = (row, col)
        print(f"Clicked cell: Row {row}, Col {col}")

cv2.namedWindow("Drone View")
cv2.setMouseCallback("Drone View", mouse_click)

while True:
    display = image.copy()
    draw_grid(display)
    if selected_cell:
        r, c = selected_cell
        x1, y1 = c * cell_w, r * cell_h
        x2, y2 = x1 + cell_w, y1 + cell_h

        cv2.rectangle(display, (x1, y1), (x2, y2), (255, 0, 0), 2)

        # Show text on screen
        cv2.putText(display, f"Cell: ({r}, {c})", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Drone View", display)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()