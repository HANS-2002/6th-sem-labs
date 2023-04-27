#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int burstTime;
    int burstTimeRemaining;
    int arrTime;
    int pid;
    int entry;
    int exit;
    int inQueue;
    int isComplete;
} process;

void swap(process *p1, process *p2)
{
    process temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void sort(process *processes, int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (processes[i].arrTime > processes[j].arrTime)
            {
                swap(&processes[i], &processes[j]);
            }
        }
    }
}

int front = -1, rear = -1, sz = 0;
process *pq[500];

void pushQueue(process *it)
{
    if (front == -1)
        front = 0;
    rear++;
    pq[rear] = it;
    sz++;
}

void popQueue()
{
    front++;
    sz--;
}

process *queueFront()
{
    return pq[front];
}

int isEmpty()
{
    return sz == 0;
}

void RR(process p[], int n, int r)
{
    int time = 0, completed = n;
    while (completed)
    {
        for (int i = 0; i < n; i++)
        {
            if (p[i].arrTime <= time && !p[i].inQueue && !p[i].isComplete)
            {
                pushQueue(&p[i]);
                p[i].inQueue = 1;
            }
        }
        process *currP = NULL;
        if (!isEmpty())
            currP = queueFront(), popQueue();
        if (currP->entry == -1)
            currP->entry = time;
        if (currP->burstTimeRemaining > r)
        {
            currP->burstTimeRemaining -= r;
            time += r;
            for (int i = 0; i < n; i++)
            {
                if (p[i].arrTime <= time && !p[i].inQueue && !p[i].isComplete)
                {
                    pushQueue(&p[i]);
                    p[i].inQueue = 1;
                }
            }
            pushQueue(currP);
        }
        else
        {
            time += currP->burstTimeRemaining;
            currP->burstTimeRemaining = 0;
            currP->isComplete = 1;
            currP->inQueue = 0;
            currP->exit = time;
            completed--;
        }
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n, q = 3;
    scanf("%d %d", &n, &q);
    process *p = (process *)malloc(n * sizeof(process));
    for (int i = 0; i < n; i++)
    {
        p[i].pid = i;
        scanf("%d %d", &p[i].arrTime, &p[i].burstTime);
        p[i].entry = -1;
        p[i].exit = -1;
        p[i].inQueue = 0;
        p[i].isComplete = 0;
        p[i].burstTimeRemaining = p[i].burstTime;
    }

    sort(p, n);
    RR(p, n, q);

    double waitTime = 0, turnTime = 0, resTime = 0;
    for (int i = 0; i < n; i++)
    {
        int tt = 0, wt = 0, rt = 0;
        tt = p[i].exit - p[i].arrTime;  // Turn Around time = Finish Time - Arrival Time
        wt = tt - p[i].burstTime;       // Waiting Time = Turn Around Time - Burst Time
        rt = p[i].entry - p[i].arrTime; // Response Time = Entry Time - Arrival Time
        waitTime += wt;
        turnTime += tt;
        resTime += rt;
    }

    printf("Round Robin (r = %d)\n", q);
    printf("Average wait time: %.2f\n", waitTime / n);
    printf("Average response time: %.2f\n", resTime / n);
    printf("Average turnaround time: %.2f\n", turnTime / n);

    return 0;
}