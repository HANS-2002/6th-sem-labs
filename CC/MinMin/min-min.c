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
    printf("\nMin-Min Scheduling:\n");
    for (int i = 0; i < number_of_processes; i++)
    {
        int min_time = INT_MAX, min_process_index = -1, min_vm_index = -1;
        for (int j = 0; j < number_of_processes; j++)
        {
            int cur_min_time = INT_MAX, cur_vm_index = -1;
            for (int k = 0; k < number_of_VM; k++)
            {
                if (table[k][j] < cur_min_time)
                {
                    cur_min_time = table[k][j];
                    cur_vm_index = k;
                }
            }
            if (cur_min_time < min_time)
            {
                min_time = cur_min_time;
                min_vm_index = cur_vm_index;
                min_process_index = j;
            }
        }
        printf("Process %d: VM %d (%d ms - %d ms)\n", min_process_index + 1, min_vm_index + 1, prevRuntimeOnVM[min_vm_index], min_time);
        prevRuntimeOnVM[min_vm_index] = min_time;
        for (int j = 0; j < number_of_processes; j++)
        {
            table[min_vm_index][j] += min_time;
        }
        for (int j = 0; j < number_of_VM; j++)
        {
            table[j][min_process_index] = INT_MAX - 100;
        }
    }
    return 0;
}