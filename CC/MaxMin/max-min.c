#include <stdio.h>
#include <limits.h>

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int number_of_VM, number_of_processes;
    scanf("%d %d", &number_of_VM, &number_of_processes);
    int table[number_of_VM][number_of_processes];
    int prevRuntimeOnVM[number_of_VM];
    for (int i = 0; i < number_of_VM; i++)
    {
        prevRuntimeOnVM[i] = 0;
        for (int j = 0; j < number_of_processes; j++)
        {
            scanf("%d", &table[i][j]);
        }
    }
    printf("Given table:\n");
    for (int i = 0; i < number_of_VM; i++)
    {
        printf("VM %d: ", i + 1);
        for (int j = 0; j < number_of_processes; j++)
        {
            printf("%d ", table[i][j]);
        }
        printf("\n");
    }
    printf("\nMax-Min Scheduling:\n");
    for (int i = 0; i < number_of_processes; i++)
    {
        int max_time = INT_MIN, max_process_index = -1, max_vm_index = -1;
        for (int j = 0; j < number_of_processes; j++)
        {
            int cur_min_time = INT_MAX, cur_vm_index = -1;
            for (int k = 0; k < number_of_VM; k++)
            {
                if (table[k][j] != -1 && table[k][j] < cur_min_time)
                {
                    cur_min_time = table[k][j];
                    cur_vm_index = k;
                }
            }
            if (cur_min_time != INT_MAX && cur_min_time > max_time)
            {
                max_time = cur_min_time;
                max_vm_index = cur_vm_index;
                max_process_index = j;
            }
        }
        printf("Process %d: VM %d (%d ms - %d ms)\n", max_process_index + 1, max_vm_index + 1, prevRuntimeOnVM[max_vm_index], max_time);
        prevRuntimeOnVM[max_vm_index] = max_time;
        for (int j = 0; j < number_of_processes; j++)
        {
            table[max_vm_index][j] += max_time;
        }
        for (int j = 0; j < number_of_VM; j++)
        {
            table[j][max_process_index] = -1;
        }
    }
    return 0;
}