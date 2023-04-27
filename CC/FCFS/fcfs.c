#include <stdio.h>

typedef struct
{
    int arrival_time;
    int burst_time;
    int completion_time;
    int turn_around_time;
    int waiting_time;
    int response_time;
} process;

void swap(process *p1, process *p2)
{
    process temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void sort(process processes[], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (processes[i].arrival_time > processes[j].arrival_time)
            {
                swap(&processes[i], &processes[j]);
            }
        }
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    scanf("%d", &n);
    process p[n];
    for (int i = 0; i < n; i++)
    {
        p[i].response_time = -1;
        p[i].waiting_time = 0;
        p[i].turn_around_time = 0;
        p[i].completion_time = 0;
        scanf("%d %d", &p[i].arrival_time, &p[i].burst_time);
    }
    sort(p, n);
    for (int i = 0; i < n; i++)
    {
        if (i == 0)
            p[i].completion_time = p[i].arrival_time + p[i].burst_time;
        else if (p[i].arrival_time > p[i - 1].completion_time)
            p[i].completion_time = p[i].arrival_time + p[i].burst_time;
        else
            p[i].completion_time = p[i - 1].completion_time + p[i].burst_time;
        p[i].turn_around_time = p[i].completion_time - p[i].arrival_time;
        p[i].waiting_time = p[i].turn_around_time - p[i].burst_time;
        p[i].response_time = p[i].waiting_time;
    }
    float avg_turn_around_time = 0, avg_waiting_time = 0, avg_response_time = 0;
    for (int i = 0; i < n; i++)
    {
        avg_turn_around_time += p[i].turn_around_time;
        avg_waiting_time += p[i].waiting_time;
        avg_response_time += p[i].response_time;
    }
    printf("FCFS Scheduling:\n");
    printf("Average Wait Time: %.2f\n", avg_waiting_time / n);
    printf("Average Response Time: %.2f\n", avg_response_time / n);
    printf("Average Turn Around Time: %.2f\n", avg_turn_around_time / n);
    return 0;
}