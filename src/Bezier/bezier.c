#include <stdio.h>
#include <graphics.h>
#include <math.h>
#include <malloc.h>
#define DEGREE 17

typedef struct
{
    float x;
    float y;
} Point;

Point AddTwoPoints(Point A, Point B)
{
    Point PointC;
    PointC.x = A.x + B.x;
    PointC.y = A.y + B.y;
    return PointC;
}

Point MultiplePoint(Point A, float k)
{
    Point PointC;
    PointC.x = k * A.x;
    PointC.y = k * A.y;
    return PointC;
}

DrawControlPolygon(Point *ControlPoints, int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        circle(ControlPoints[i].x, ControlPoints[i].y, 5);
        setfillstyle(1, 4);
        floodfill(ControlPoints[i].x, ControlPoints[i].y, 4);
    }
    moveto(ControlPoints[0].x, ControlPoints[0].y);
    for (i = 1; i < n; i++)
    {
        setlinestyle(DASHED_LINE, 0, 0);
        moveto(ControlPoints[i - 1].x, ControlPoints[i - 1].y);
        lineto(ControlPoints[i].x, ControlPoints[i].y);
    }
}

Point CalculateBezierPoint(Point *ControlPoints, int n, float t)
{
    int i;
    Point NextControlPoints[DEGREE - 1];
    for (i = 0; i < n - 1; i++)
    {
        NextControlPoints[i] = AddTwoPoints(MultiplePoint(ControlPoints[i], 1 - t),
                                            MultiplePoint(ControlPoints[i + 1], t));
    }
    if (n == 2)
    {
        return NextControlPoints[0];
    }
    else
    {
        return CalculateBezierPoint(NextControlPoints, n - 1, t);
    }
}

DrawBezierCurve(Point *ControlPoints)
{
    Point CurvePoint;
    float t;
    char str[3];
    CurvePoint = CalculateBezierPoint(ControlPoints, DEGREE, 0);
    for (t = 0; t <= 1.00001; t = t + 0.01)
    {
        moveto(CurvePoint.x, CurvePoint.y);
        CurvePoint = CalculateBezierPoint(ControlPoints, DEGREE, t);
        lineto(CurvePoint.x, CurvePoint.y);
        /*circle(CurvePoint.x, CurvePoint.y, 10);*/
    }
}

void main()
{
    int drive = VGA, mode = VGAHI;
    Point ControlPoints1[17] = {
        {80, 450},
        {100, 400},
        {120, 350},
        {140, 300},
        {160, 250},
        {180, 200},
        {200, 150},
        {250, 150},
        {300, 150},
        {350, 150},
        {400, 150},
        {420, 200},
        {440, 250},
        {460, 300},
        {480, 350},
        {500, 400},
        {520, 450},
    };

    Point ControlPoints2[17] = {
        {100, 450},
        {100, 350},
        {100, 250},
        {100, 150},
        {150, 150},
        {200, 150},
        {250, 150},
        {250, 250},
        {250, 350},
        {250, 450},
        {300, 450},
        {350, 450},
        {400, 450},
        {450, 450},
        {450, 350},
        {450, 250},
        {450, 150},
    };

    Point ControlPoints3[17] = {
        {100, 450},
        {120, 150},
        {140, 450},
        {160, 150},
        {180, 450},
        {200, 150},
        {220, 450},
        {240, 150},
        {260, 450},
        {280, 150},
        {300, 450},
        {320, 150},
        {340, 450},
        {360, 150},
        {380, 450},
        {400, 150},
        {420, 450},
    };

    /*First Example 初始化图形设备，设置背景*/
    initgraph(&drive, &mode, "C:\\TC20\\BGI");
    setbkcolor(15);
    setcolor(4);

    settextstyle(DEFAULT_FONT, HORIZ_DIR, 2);
    outtextxy(200, 30, "First Example");
    outtextxy(70, 80, "(Print any keyboard to continue)");
    DrawControlPolygon(ControlPoints1, DEGREE);
    setlinestyle(SOLID_LINE, 0, THICK_WIDTH);
    DrawBezierCurve(ControlPoints1);
    getch();
    closegraph();

    /*Second Example 初始化图形设备，设置背景*/
    initgraph(&drive, &mode, "C:\\TC20\\BGI");
    setbkcolor(15);
    setcolor(4);

    settextstyle(DEFAULT_FONT, HORIZ_DIR, 2);
    outtextxy(200, 30, "Second Example");
    outtextxy(70, 80, "(Print any keyboard to continue)");
    DrawControlPolygon(ControlPoints2, DEGREE);
    setlinestyle(SOLID_LINE, 0, THICK_WIDTH);
    DrawBezierCurve(ControlPoints2);
    getch();
    closegraph();

    /*Last Example 初始化图形设备，设置背景*/
    initgraph(&drive, &mode, "C:\\TC20\\BGI");
    setbkcolor(15);
    setcolor(4);

    settextstyle(DEFAULT_FONT, HORIZ_DIR, 2);
    outtextxy(200, 30, "Last Example");
    outtextxy(70, 80, "(Print any keyboard to exit)");
    DrawControlPolygon(ControlPoints3, DEGREE);
    setlinestyle(SOLID_LINE, 0, THICK_WIDTH);
    DrawBezierCurve(ControlPoints3);
    delay(500);
    outtextxy(360, 200, "Unexpected Result");
    outtextxy(390, 250, "But Reasonable");
    getch();
    closegraph();
}