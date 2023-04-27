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

void SRTN(process p[], int n)
{
    int current_time = 0;
    int completed = 0;
    int prev = 0;

    while (completed != n)
    {
        int idx = -1;
        int mn = 10000000;
        for (int i = 0; i < n; i++)
        {
            if (p[i].arrTime <= current_time && p[i].isComplete == 0)
            {
                if (p[i].burstTimeRemaining < mn)
                {
                    mn = p[i].burstTimeRemaining;
                    idx = i;
                }
                if (p[i].burstTimeRemaining == mn)
                {
                    if (p[i].arrTime < p[idx].arrTime)
                    {
                        mn = p[i].burstTimeRemaining;
                        idx = i;
                    }
                }
            }
        }

        if (idx != -1)
        {
            if (p[idx].burstTimeRemaining == p[idx].burstTime)
            {
                p[idx].entry = current_time;
            }
            p[idx].burstTimeRemaining -= 1;
            current_time++;
            prev = current_time;

            if (p[idx].burstTimeRemaining == 0)
            {
                p[idx].exit = current_time;
                p[idx].isComplete = 1;
                completed++;
            }
        }
        else
        {
            current_time++;
        }
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    scanf("%d", &n);
    process *p = (process *)malloc(n * sizeof(process));
    for (int i = 0; i < n; i++)
    {
        p[i].pid = i;
        scanf("%d %d", &p[i].arrTime, &p[i].burstTime);
        p[i].entry = -1;
        p[i].exit = -1;
        p[i].isComplete = 0;
        p[i].burstTimeRemaining = p[i].burstTime;
    }

    sort(p, n);
    SRTN(p, n);

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

    printf("SRTN Scheduling:\n");
    printf("Average wait time: %.2f\n", waitTime / n);
    printf("Average response time: %.2f\n", resTime / n);
    printf("Average turnaround time: %.2f\n", turnTime / n);

    return 0;
}