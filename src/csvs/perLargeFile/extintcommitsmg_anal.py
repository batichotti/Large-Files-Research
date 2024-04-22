import os
import pandas as pd

os.system('clear')

def read_large_files_data(folder_path:str):
    dataframes = []
    for folder in os.listdir(folder_path):
        folder_full_path = os.path.join(folder_path, folder)
        if os.path.isdir(folder_full_path):
            for file in os.listdir(folder_full_path):
                file_full_path = os.path.join(folder_full_path, file)
                if os.path.isdir(file_full_path):
                    for each in os.listdir(file_full_path):
                        each_full_path = os.path.join(file_full_path, each)
                        if each.endswith("csv_mgcommit_anal.csv"):
                            print("Processing CSV file:", each_full_path)
                            df = pd.read_csv(each_full_path)
                            df['Project'] = folder
                            dataframes.append(df)
    os.system('clear')
    return pd.concat(dataframes, ignore_index=True)

def percent(num:int, total:int) -> float:
    return num*100/total

def one_and_rest_percent(idx:int, list:list) -> tuple:
    temp = 0
    for i in range(len(list)):
        temp += list[i]
    return percent(list[idx],temp), percent(temp-list[idx], temp)



def main():
    #Arquivos Grandes
    folder_path_large_files = os.path.join("src", "csvs", "perLargeFile", "extint")
    commits = read_large_files_data(folder_path_large_files)
    hashs = []

    commitop = []
    buildc = []
    bug = []
    feature = []
    refactoring = []
    optimazing = []
    test = []
    tangled = []
    bug_tangle = []
    fet_tangle = []
    ref_tangle = []
    other = []

    for i in range(len(commits)):
        os.system('clear')
        print(f'{i*100/len(commits):.2f}%')
        if commits['Hash'].loc[i] not in hashs:
            if "Tangled Commits" in commits['Commit Purpose'].loc[i]:
                tangled.append(commits['Hash'].loc[i])
                if "Bug-Fix" in commits['Commit Purpose'].loc[i]:
                    bug_tangle.append(commits['Hash'].loc[i])
                if "New Feature" in commits['Commit Purpose'].loc[i]:
                    fet_tangle.append(commits['Hash'].loc[i])
                if "Refactoring" in commits['Commit Purpose'].loc[i]:
                    ref_tangle.append(commits['Hash'].loc[i])
            elif "Commit Operation" in commits['Commit Purpose'].loc[i]:
                commitop.append(commits['Hash'].loc[i])
            elif "Build Configuration" in commits['Commit Purpose'].loc[i]:
                buildc.append(commits['Hash'].loc[i])
            elif "Bug-Fix" in commits['Commit Purpose'].loc[i]:
                bug.append(commits['Hash'].loc[i])
            elif "New Feature" in commits['Commit Purpose'].loc[i]:
                feature.append(commits['Hash'].loc[i])
            elif "Refactoring" in commits['Commit Purpose'].loc[i]:
                refactoring.append(commits['Hash'].loc[i])
            elif "Optimizing" in commits['Commit Purpose'].loc[i]:
                optimazing.append(commits['Hash'].loc[i])
            elif "Test" in commits['Commit Purpose'].loc[i]:
                test.append(commits['Hash'].loc[i])
            else:
                other.append(commits['Hash'].loc[i])
            hashs.append(commits['Hash'].loc[i])

    total = len(hashs)
    tcommit = len(commitop)
    tbuild = len(buildc)
    tbug = len(bug)
    tnewf = len(feature)
    trefact = len(refactoring)
    topt = len(optimazing)
    ttest = len(test)
    ttangled = len(tangled)
    tother = len(other)

    tbug_tangle = len(bug_tangle)
    tfet_tangle = len(fet_tangle)
    tref_tangle = len(ref_tangle)

    #Arquivos não grandes
    folder_path_large_files = os.path.join("src", "csvs", "perLargeFile", "tinyextint")
    commits_tiny = read_large_files_data(folder_path_large_files)
    tiny_hashs = []


    tiny_commitop = []
    tiny_buildc = []
    tiny_bug = []
    tiny_feature = []
    tiny_refactoring = []
    tiny_tangled = []
    tiny_optimazing = []
    tiny_test = []
    tiny_bug_tangle = []
    tiny_fet_tangle = []
    tiny_ref_tangle = []
    tiny_other = []

    for i in range(len(commits_tiny)):
        os.system('clear')
        print(f'{i*100/len(commits_tiny):.2f}%')
        if commits_tiny['Hash'].loc[i] not in tiny_hashs:
            if "Tangled Commits" in commits_tiny['Commit Purpose'].loc[i]:
                tiny_tangled.append(commits_tiny['Hash'].loc[i])
                if "Bug-Fix" in commits_tiny['Commit Purpose'].loc[i]:
                    tiny_bug_tangle.append(commits_tiny['Hash'].loc[i])
                if "New Feature" in commits_tiny['Commit Purpose'].loc[i]:
                    tiny_fet_tangle.append(commits_tiny['Hash'].loc[i])
                if "Refactoring" in commits_tiny['Commit Purpose'].loc[i]:
                    tiny_ref_tangle.append(commits_tiny['Hash'].loc[i])
            elif "Commit Operation" in commits_tiny['Commit Purpose'].loc[i]:
                tiny_commitop.append(commits_tiny['Hash'].loc[i])
            elif "Build Configuration" in commits_tiny['Commit Purpose'].loc[i]:
                tiny_buildc.append(commits_tiny['Hash'].loc[i])
            elif "Bug-Fix" in commits_tiny['Commit Purpose'].loc[i]:
                tiny_bug.append(commits_tiny['Hash'].loc[i])
            elif "New Feature" in commits_tiny['Commit Purpose'].loc[i]:
                tiny_feature.append(commits_tiny['Hash'].loc[i])
            elif "Refactoring" in commits_tiny['Commit Purpose'].loc[i]:
                tiny_refactoring.append(commits_tiny['Hash'].loc[i])
            elif "Optimizing" in commits_tiny['Commit Purpose'].loc[i]:
                tiny_optimazing.append(commits_tiny['Hash'].loc[i])
            elif "Test" in commits_tiny['Commit Purpose'].loc[i]:
                tiny_test.append(commits_tiny['Hash'].loc[i])
            else:
                tiny_other.append(commits_tiny['Hash'].loc[i])
            tiny_hashs.append(commits_tiny['Hash'].loc[i])


    tiny_total = len(tiny_hashs)

    ttiny_commit = len(tiny_commitop)
    ttiny_build = len(tiny_buildc)
    ttiny_bug = len(tiny_bug)
    ttiny_newf = len(tiny_feature)
    ttiny_refact = len(tiny_refactoring)
    ttiny_tangled = len(tiny_tangled)
    ttiny_opt = len(tiny_optimazing)
    ttiny_test = len(tiny_test)
    ttiny_bug_tangle = len(tiny_bug_tangle)
    ttiny_fet_tangle = len(tiny_fet_tangle)
    ttiny_ref_tangle = len(tiny_ref_tangle)
    ttiny_other = len(tiny_other)

    #Resultado
    print(f'''
Total 199 Internal Large Files-> {total}
Commit Operation -> {tcommit}
Build Configuration -> {tbuild}
Bug-Fix -> {tbug}
New Feature -> {tnewf}
Refactoring -> {trefact}
Optimizing -> {topt}
Test -> {ttest}
Tangled Commits -> {ttangled}
    Bug-Fix -> {tbug_tangle}
    New Feature -> {tfet_tangle}
    Refactoring -> {tref_tangle}
Other -> {tother}

Porcentis
Commit Operation -> {percent(tcommit,total):.2f}%
Build Configuration -> {percent(tbuild,total):.2f}%
Bug-Fix -> {percent(tbug,total):.2f}%
New Feature -> {percent(tnewf,total):.2f}%
Refactoring -> {percent(trefact,total):.2f}%
Optimizing -> {percent(topt,total):.2f}%
Test -> {percent(ttest,total):.2f}%
Tangled Commits -> {percent(ttangled,total):.2f}%
    Bug-Fix -> {percent(tbug_tangle, ttangled):.2f}%
    New Feature -> {percent(tfet_tangle, ttangled):.2f}%
    Refactoring -> {percent(tref_tangle, ttangled):.2f}%
Other -> {percent(tother,total):.2f}%

---------------------------------------

Total 199 Tiny Files
Total Tiny Files-> {tiny_total}
Commit Operation -> {ttiny_commit}
Build Configuration -> {ttiny_build}
Bug-Fix -> {ttiny_bug}
New Feature -> {ttiny_newf}
Refactoring -> {ttiny_refact}
Optimizing -> {ttiny_opt}
Test -> {ttiny_test}
Tangled Commits -> {ttiny_tangled}
    Bug-Fix -> {ttiny_bug_tangle}
    New Feature -> {ttiny_fet_tangle}
    Refactoring -> {ttiny_ref_tangle}
Other -> {ttiny_other}

Porcentis
Commit Operation -> {percent(ttiny_commit,tiny_total):.2f}%
Build Configuration -> {percent(ttiny_build,tiny_total):.2f}%
Bug-Fix -> {percent(ttiny_bug,tiny_total):.2f}%
New Feature -> {percent(ttiny_newf,tiny_total):.2f}%
Refactoring -> {percent(ttiny_refact,tiny_total):.2f}%
Optimizing -> {percent(ttiny_opt,tiny_total):.2f}%
Test -> {percent(ttiny_test,tiny_total):.2f}%
Tangled Commits -> {percent(ttiny_tangled,tiny_total):.2f}%
    Bug-Fix -> {percent(ttiny_bug_tangle, ttiny_tangled):.2f}%
    New Feature -> {percent(ttiny_fet_tangle, ttiny_tangled):.2f}%
    Refactoring -> {percent(ttiny_ref_tangle, ttiny_tangled):.2f}%
Other -> {percent(ttiny_other,tiny_total):.2f}%

-----------------------------------------

Bug-Fix x Não Bug-Fix
Arquivos Grandes -> {one_and_rest_percent(0, [tbug, tnewf, trefact])}
Arquivos Não Grandes -> {one_and_rest_percent(0, [ttiny_bug, ttiny_newf, ttiny_refact])}

New Feature x Não New Feature
Arquivos Grandes -> {one_and_rest_percent(1, [tbug, tnewf, trefact])}
Arquivos Não Grandes -> {one_and_rest_percent(1, [ttiny_bug, ttiny_newf, ttiny_refact])}

Refactoring x Não Refactoring
Arquivos Grandes -> {one_and_rest_percent(2, [tbug, tnewf, trefact])}
Arquivos Não Grandes -> {one_and_rest_percent(2, [ttiny_bug, ttiny_newf, ttiny_refact])}
''')

if __name__ == "__main__":
    main()
