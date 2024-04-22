from pydriller import Repository
import pandas as pd
import os
from random import randint

repositories = ['https://github.com/nodejs/node', 'https://github.com/matomo-org/matomo', 'https://github.com/vuejs/core', 'https://github.com/facebook/react','https://github.com/microsoft/TypeScript','https://github.com/facebook/react-native']
errors = []

def dataFramer(commit, file):
    summary = pd.DataFrame({
        'Hash': [commit.hash],
        'Project Name': [commit.project_name],
        'Local Commit PATH': [commit.project_path],
        'Message': [commit.msg],
        'Main Branch': [commit.in_main_branch],
        'Number of Files': [commit.files],
        'Modified Lines': [commit.lines],
        'File Name': [file.filename],
        'Change Type': [str(file.change_type).split('.')[-1]],
        'Local File PATH Old': [file.old_path if file.old_path else 'none'],
        'Local File PATH New': [file.new_path],
        'Author Name': [commit.author.name],
        'Author Email': [commit.author.email],
        'Author Commit Date': [commit.author_date],
        'Author Commit Timezone': [commit.author_timezone],
        'Committer Name': [commit.committer.name],
        'Committer Email': [commit.committer.email],
        'Committer Commit Date': [commit.committer_date],
        'Committer Timezone': [commit.committer_timezone],
        'Merge Commit': [commit.merge],
        'Complexity': [file.complexity if file.complexity else 'null'],
        'Methods': [len(file.methods)],
        'Tokens': [file.token_count if file.token_count else 'null'],
        'Lines Of Code(nloc)': [file.nloc if file.nloc else 'null'],
        'Lines Added': [file.added_lines],
        'Lines Deleted': [file.deleted_lines],
        'Lines Modified per File': [file.added_lines + file.deleted_lines],
        'Lines Balance': [file.added_lines - file.deleted_lines]
    })
    if not os.path.isfile(f'csvs/{commit.project_name}.csv'):
        summary.to_csv(f'csvs/{commit.project_name}.csv', index=False)
    else:
        summary.to_csv(f'csvs/{commit.project_name}.csv', index=False, mode='a', header=False)


repositories_js2 = [
    'https://github.com/basecamp/trix'
]

repositories_js = [
    'https://github.com/Alamofire/Alamofire',
    'https://github.com/angular/angular-cli',
    'https://github.com/angular/angular',
    'https://github.com/angular/angular.js',
    'https://github.com/ant-design/ant-design',
    'https://github.com/apache/arrow',
    'https://github.com/atom/atom',
    'https://github.com/BabylonJS/Babylon.js',
    'https://github.com/jashkenas/backbone',
    'https://github.com/baconjs/bacon.js',
    'https://github.com/twbs/bootstrap',
    'https://github.com/twbs/bootstrap-sass',
    'https://github.com/microsoft/botframework-sdk',
    'https://github.com/adobe/brackets',
    'https://github.com/chartjs/Chart.js',
    'https://github.com/gka/chroma.js',
    'https://github.com/codecombat/codecombat',
    'https://github.com/jashkenas/coffeescript',
    'https://github.com/hashicorp/consul',
    'https://github.com/facebook/create-react-app',
    'https://github.com/ValtoGameEngines/CryEngine',
    'https://github.com/discourse/discourse',
    'https://github.com/django/django',
    'https://github.com/electron/electron',
    'https://github.com/emscripten-core/emscripten',
    'https://github.com/jquery/esprima',
    'https://github.com/smpallen99/ex_admin',
    'https://github.com/foundation/foundation-sites',
    'https://github.com/facebook/fresco',
    'https://github.com/gatling/gatling',
    'https://github.com/ghcjs/ghcjs',
    'https://github.com/gitbucket/gitbucket',
    'https://github.com/jgm/gitit',
    'https://github.com/gitlabhq/gitlabhq',
    'https://github.com/gogs/gogs',
    'https://github.com/grafana/grafana',
    'https://github.com/h2o/h2o',
    'https://github.com/valderman/haste-compiler',
    'https://github.com/HeroTransitions/Hero',
    'https://github.com/huginn/huginn',
    'https://github.com/impress/impress.js',

    'https://github.com/ionic-team/ionic-framework',
    'https://github.com/blueimp/jQuery-File-Upload',
    'https://github.com/jquery/jquery',
    'https://github.com/bang590/JSPatch',
    'https://github.com/Kitura/Kitura',
    'https://github.com/getlantern/lantern',
    'https://github.com/bhauman/lein-figwheel',
    'https://github.com/lichess-org/lila',
    'https://github.com/linkerd/linkerd',
    'https://github.com/MarathonLabs/marathon',
    'https://github.com/mui/material-ui',
    'https://github.com/MaterialDesignInXAML/MaterialDesignInXamlToolkit',
    'https://github.com/MaterializeInc/materialize',
    'https://github.com/matomo-org/matomo',

    'https://github.com/meteor/meteor',
    'https://github.com/moment/moment',
    'https://github.com/mono/mono',
    'https://github.com/morrisjs/morris.js',
    'https://github.com/NancyFx/Nancy',
    'https://github.com/netdata/netdata',
    'https://github.com/ng-bootstrap/ng-bootstrap',
    #'https://github.com/nodejs/node',

    'https://github.com/nwjs/nw.js',
    'https://github.com/sumsuddin/openface',
    'https://github.com/opserver/Opserver',
    'https://github.com/foliojs/pdfkit',
    'https://github.com/phacility/phabricator',
    'https://github.com/php/php-src', #2001 #reestrair
    'https://github.com/nicolaskruchten/pivottable',
    'https://github.com/graphile/postgraphile',
    'https://github.com/prometheus/prometheus',
    'https://github.com/protocolbuffers/protobuf-javascript',
    'https://github.com/Quick/Quick',
    'https://github.com/rails/rails',
    'https://github.com/day8/re-frame',
    #'https://github.com/facebook/react-native',
    #'https://github.com/facebook/react',

    'https://github.com/reddit-archive/reddit',
    'https://github.com/rethinkdb/admin',
    'https://github.com/hakimel/reveal.js',
    'https://github.com/rust-lang/rust', #
    'https://github.com/ReactiveX/RxSwift',

    'https://github.com/sailorproject/sailor',
    'https://github.com/sahat/satellizer',
    'https://github.com/Semantic-Org/Semantic-UI',
    'https://github.com/getsentry/sentry',
    'https://github.com/ServiceStack/ServiceStack',
    'https://github.com/overleaf/overleaf',
    'https://github.com/mozilla/shumway',
    'https://github.com/SignalR/SignalR',
    'https://github.com/socketio/socket.io',
    'https://github.com/spray/spray',
    'https://github.com/spring-projects/spring-boot',
    'https://github.com/FelisCatus/SwitchyOmega',
    'https://github.com/syncthing/syncthing',
    'https://github.com/mrdoob/three.js',
    #https://github.com/basecamp/trix,
    #'https://github.com/microsoft/TypeScript',
    'https://github.com/angular-ui/ui-router',
    'https://github.com/v8/v8',
    'https://github.com/fossasia/visdom',
    'https://github.com/microsoft/vscode',
    'https://github.com/vuejs/vue',
    'https://github.com/webpack/webpack',
    'https://github.com/winjs/winjs',
    'https://github.com/WordPress/WordPress',
    'https://github.com/yarnpkg/yarn',
    'https://github.com/yiisoft/yii2',
    'https://github.com/HelloZeroNet/ZeroNet',
    'https://github.com/dropbox/zxcvbn'

    ]
idx = 0

for i in range(idx, len(repositories_js2)):
    repo = Repository(repositories_js2[i], only_no_merge = True)
    print(repositories_js2[i])

    for commit in repo.traverse_commits():
        try:
            for file in commit.modified_files:
                dataFramer(commit, file)
                print(f"\033[3{randint(0, 7)}m {commit.committer_date}")
        except Exception as e:
            print(f'Error: {e}')
            errors.append(e)
            df = pd.DataFrame({'Error': errors})
            df = df.reset_index()
            df.columns = ['Index', 'Error']
            df.to_csv(f'errors/errors_{commit.project_name}.csv', mode='a', header=False)
