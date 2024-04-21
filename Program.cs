using System;
using System.Diagnostics;

namespace VK_TEST
{
    class Program
    {
        static void Main()
        {
            int pid = 0;
            bool flag = true;
            Process[] processes = Process.GetProcesses();
            Process proc;
            foreach (Process item in processes)
            {
                Console.WriteLine("Name: {0}  PID: {1}", item.ProcessName, item.Id);
            }
            Console.WriteLine("\nIf you want to exit enter -1");
            while (flag)
            {
                try
                {
                    Console.Write("Please enter PID of process you want to kill: ");
                    pid = Convert.ToInt32(Console.ReadLine());
                    proc = Process.GetProcessById(pid);
                    proc.Kill();
                    flag = false;
                    Console.WriteLine("\nProcess with PID {0} has been killed! Congratulations!", pid);
                }
                catch (FormatException)
                {
                    Console.WriteLine("You should enter a number!");
                }
                catch (ArgumentException)
                {
                    if (pid == -1)
                    {
                        break;
                    }
                    else if (pid < 1 || pid > 32768)
                    {
                        Console.WriteLine("PID have to be from 1 to 32768!");
                    }
                    else
                    {
                        Console.WriteLine("Process with PID {0} is not running!", pid);
                    }
                }
                catch (OverflowException)
                {
                    Console.WriteLine("PID have to be from 1 to 32768!");
                }
                catch (Exception exception)
                {
                    Console.WriteLine(exception.Message);
                }
            }
        }
        //Как вариант прописать все исключения в Exception, ипользуя is и switch/if
    }
}
