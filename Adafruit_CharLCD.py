  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCD/Adafruit_CharLCD.py at master · adafruit/Adafruit-Raspberry-Pi-Python-Code</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <link rel="assets" href="https://a248.e.akamai.net/assets.github.com/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="4710252" name="octolytics-actor-id" /><meta content="eiktyrner" name="octolytics-actor-login" /><meta content="5899b6bcfce06923b8adc75e0d6feea071e28b4c42648b220afdc8ee69ba3ae4" name="octolytics-actor-hash" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="ORnuAlIdj/Fm41g+lMvSlPJFlKmL7/16PWI9m+a5QX0=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-81b13ea53b1680d36f84ba58001e4a489c3f99d2.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-8b9943a538de5ba2343c96854d47c48eb6f2da5d.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-4c434fa1705bf526e191eec0cd8fab1a5ce3e326.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-5e72c8897c5b4f51f6829429a2f0045853a2cf36.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="541ec61f9d9c0a273af8ee8616e5fc81">

        <link data-pjax-transient rel='permalink' href='/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/501c1cebfe579c51f00b0749ef450a6476ac9375/Adafruit_CharLCD/Adafruit_CharLCD.py'>
    <meta property="og:title" content="Adafruit-Raspberry-Pi-Python-Code"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/4bc2305bba6e4c82a64a8706ae8b3d40?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="Adafruit-Raspberry-Pi-Python-Code - Adafruit library code for Raspberry Pi"/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="adafruit/Adafruit-Raspberry-Pi-Python-Code"/>

    <meta name="description" content="Adafruit-Raspberry-Pi-Python-Code - Adafruit library code for Raspberry Pi" />


    <meta content="181069" name="octolytics-dimension-user_id" /><meta content="adafruit" name="octolytics-dimension-user_login" /><meta content="5383151" name="octolytics-dimension-repository_id" /><meta content="adafruit/Adafruit-Raspberry-Pi-Python-Code" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="5383151" name="octolytics-dimension-repository_network_root_id" /><meta content="adafruit/Adafruit-Raspberry-Pi-Python-Code" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master.atom" rel="alternate" title="Recent Commits to Adafruit-Raspberry-Pi-Python-Code:master" type="application/atom+xml" />

  </head>


  <body class="logged_in page-blob windows vis-public env-production  ">
    <div id="wrapper">

      
      
      

      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    <div class="divider-vertical"></div>

      <a href="/notifications" class="notification-indicator tooltipped downwards" title="You have no unread notifications">
    <span class="mail-status all-read"></span>
  </a>
  <div class="divider-vertical"></div>


      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">
  <a href="/search/advanced" class="advanced-search-icon tooltipped downwards command-bar-search" id="advanced_search" title="Advanced search"><span class="octicon octicon-gear "></span></a>

  <input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    data-username="eiktyrner"
      data-repo="adafruit/Adafruit-Raspberry-Pi-Python-Code"
      data-branch="master"
      data-sha="a66430a555e5300e59546b4703dc867f1d7957bf"
  >

    <input type="hidden" name="nwo" value="adafruit/Adafruit-Raspberry-Pi-Python-Code" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

  <div class="divider-vertical"></div>

</form>
        <ul class="top-nav">
            <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="http://help.github.com">Help</a></li>
        </ul>
      </div>

    

  

    <ul id="user-links">
      <li>
        <a href="/eiktyrner" class="name">
          <img height="20" src="https://secure.gravatar.com/avatar/eb58a81e3c23c9f40bcf9b0c5703158b?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /> eiktyrner
        </a>
      </li>

        <li>
          <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a new repo">
            <span class="octicon octicon-repo-create"></span>
          </a>
        </li>

        <li>
          <a href="/settings/profile" id="account_settings"
            class="tooltipped downwards"
            title="Account settings ">
            <span class="octicon octicon-tools"></span>
          </a>
        </li>
        <li>
          <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out">
            <span class="octicon octicon-log-out"></span>
          </a>
        </li>

    </ul>


<div class="js-new-dropdown-contents hidden">
  <ul class="dropdown-menu">
    <li>
      <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
    </li>
    <li>
        <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
    </li>
    <li>
    </li>
    <li>
      <a href="/organizations/new"><span class="octicon octicon-list-unordered"></span> New organization</a>
    </li>
  </ul>
</div>


    
  </div>
</div>

      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              

<ul class="pagehead-actions">


    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="ORnuAlIdj/Fm41g+lMvSlPJFlKmL7/16PWI9m+a5QX0=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="5383151" />

    <div class="select-menu js-menu-container js-select-menu">
      <span class="minibutton select-menu-button  js-menu-target">
        <span class="js-select-button">
          <span class="octicon octicon-eye-watch"></span>
          Watch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container">

            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for discussions in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

    <li class="js-toggler-container js-social-container starring-container ">
      <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/unstar" class="minibutton with-count js-toggler-target star-button starred upwards" title="Unstar this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="octicon octicon-star-delete"></span>
        <span class="text">Unstar</span>
      </a>
      <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/star" class="minibutton with-count js-toggler-target star-button unstarred upwards" title="Star this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="octicon octicon-star"></span>
        <span class="text">Star</span>
      </a>
      <a class="social-count js-social-count" href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/stargazers">199</a>
    </li>

        <li>
          <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/fork" class="minibutton with-count js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="nofollow" data-method="post">
            <span class="octicon octicon-git-branch-create"></span>
            <span class="text">Fork</span>
          </a>
          <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/network" class="social-count">106</a>
        </li>


</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-octicon octicon-repo"></span>
                <span class="author vcard">
                  <a href="/adafruit" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">adafruit</span>
                  </a></span> /
                <strong><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code" class="js-current-repository">Adafruit-Raspberry-Pi-Python-Code</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li class="pulse-nav"><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/pulse" class="js-selected-navigation-item " data-selected-links="pulse /adafruit/Adafruit-Raspberry-Pi-Python-Code/pulse" rel="nofollow"><span class="octicon octicon-pulse"></span></a></li>
    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code" class="js-selected-navigation-item selected" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /adafruit/Adafruit-Raspberry-Pi-Python-Code">Code</a></li>
    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/network" class="js-selected-navigation-item " data-selected-links="repo_network /adafruit/Adafruit-Raspberry-Pi-Python-Code/network">Network</a></li>
    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/pulls" class="js-selected-navigation-item " data-selected-links="repo_pulls /adafruit/Adafruit-Raspberry-Pi-Python-Code/pulls">Pull Requests <span class='counter'>7</span></a></li>

      <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/issues" class="js-selected-navigation-item " data-selected-links="repo_issues /adafruit/Adafruit-Raspberry-Pi-Python-Code/issues">Issues <span class='counter'>18</span></a></li>

      <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/wiki" class="js-selected-navigation-item " data-selected-links="repo_wiki /adafruit/Adafruit-Raspberry-Pi-Python-Code/wiki">Wiki</a></li>


    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/graphs" class="js-selected-navigation-item " data-selected-links="repo_graphs repo_contributors /adafruit/Adafruit-Raspberry-Pi-Python-Code/graphs">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/tags" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_tags /adafruit/Adafruit-Raspberry-Pi-Python-Code/tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="octicon octicon-git-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item selected">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_CharLCD/Adafruit_CharLCD.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <div class="select-menu-no-results">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code" class="selected js-selected-navigation-item tabnav-tab" data-selected-links="repo_source /adafruit/Adafruit-Raspberry-Pi-Python-Code">Files</a></li>
    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_commits /adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master">Commits</a></li>
    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/branches" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_branches /adafruit/Adafruit-Raspberry-Pi-Python-Code/branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:6b52456b4943a692eeff654b3242b1e8 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:6b52456b4943a692eeff654b3242b1e8 -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">Adafruit-Raspberry-Pi-Python-Code</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCD" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">Adafruit_CharLCD</span></a></span><span class="separator"> / </span><strong class="final-path">Adafruit_CharLCD.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="Adafruit_CharLCD/Adafruit_CharLCD.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
        </div>

      <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/60c89f8d785a4b4afa6a799bd1059625?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><a href="/rogg" rel="author">rogg</a></span>
    <time class="js-relative-date" datetime="2012-12-02T05:04:07-08:00" title="2012-12-02 05:04:07">December 02, 2012</time>
    <div class="commit-title">
        <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commit/fb6b7f591c1b2c352347bf0044ebc3765d450310" class="message">Update Adafruit_CharLCD/Adafruit_CharLCD.py</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>3</strong> contributors</a></p>
          <a class="avatar tooltipped downwards" title="ladyada" href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master/Adafruit_CharLCD/Adafruit_CharLCD.py?author=ladyada"><img height="20" src="https://secure.gravatar.com/avatar/3f7ca151e1f7f7dead8b2db60aa744c1?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="dberlin" href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master/Adafruit_CharLCD/Adafruit_CharLCD.py?author=dberlin"><img height="20" src="https://secure.gravatar.com/avatar/96a1083a4171c9b2a684f538d2782bdd?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="rogg" href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master/Adafruit_CharLCD/Adafruit_CharLCD.py?author=rogg"><img height="20" src="https://secure.gravatar.com/avatar/60c89f8d785a4b4afa6a799bd1059625?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li class="facebox-user-list-item">
          <img height="24" src="https://secure.gravatar.com/avatar/3f7ca151e1f7f7dead8b2db60aa744c1?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/ladyada">ladyada</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://secure.gravatar.com/avatar/96a1083a4171c9b2a684f538d2782bdd?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/dberlin">dberlin</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://secure.gravatar.com/avatar/60c89f8d785a4b4afa6a799bd1059625?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/rogg">rogg</a>
        </li>
      </ul>
    </div>
  </div>


    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/501c1cebfe579c51f00b0749ef450a6476ac9375/Adafruit_CharLCD/Adafruit_CharLCD.py" data-title="Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCD/Adafruit_CharLCD.py at master · adafruit/Adafruit-Raspberry-Pi-Python-Code · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="octicon octicon-file-text"></b></span>
                <span class="mode" title="File Mode">executable file</span>
                  <span>262 lines (170 sloc)</span>
                <span>7.03 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                        <a class="minibutton tooltipped leftwards"
                           title="Clicking this button will automatically fork this project so you can edit the file"
                           href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/edit/master/Adafruit_CharLCD/Adafruit_CharLCD.py"
                           data-method="post" rel="nofollow">Edit</a>
                  <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/raw/master/Adafruit_CharLCD/Adafruit_CharLCD.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/blame/master/Adafruit_CharLCD/Adafruit_CharLCD.py" class="button minibutton ">Blame</a>
                  <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master/Adafruit_CharLCD/Adafruit_CharLCD.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/python</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="c">#</span></div><div class='line' id='LC4'><span class="c"># based on code from lrvick and LiquidCrystal</span></div><div class='line' id='LC5'><span class="c"># lrvic - https://github.com/lrvick/raspi-hd44780/blob/master/hd44780.py</span></div><div class='line' id='LC6'><span class="c"># LiquidCrystal - https://github.com/arduino/Arduino/blob/master/libraries/LiquidCrystal/LiquidCrystal.cpp</span></div><div class='line' id='LC7'><span class="c">#</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">sleep</span></div><div class='line' id='LC10'><br/></div><div class='line' id='LC11'><span class="k">class</span> <span class="nc">Adafruit_CharLCD</span><span class="p">:</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># commands</span></div><div class='line' id='LC14'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_CLEARDISPLAY</span> 		<span class="o">=</span> <span class="mh">0x01</span></div><div class='line' id='LC15'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_RETURNHOME</span> 		<span class="o">=</span> <span class="mh">0x02</span></div><div class='line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_ENTRYMODESET</span> 		<span class="o">=</span> <span class="mh">0x04</span></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_DISPLAYCONTROL</span> 		<span class="o">=</span> <span class="mh">0x08</span></div><div class='line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_CURSORSHIFT</span> 		<span class="o">=</span> <span class="mh">0x10</span></div><div class='line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_FUNCTIONSET</span> 		<span class="o">=</span> <span class="mh">0x20</span></div><div class='line' id='LC20'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_SETCGRAMADDR</span> 		<span class="o">=</span> <span class="mh">0x40</span></div><div class='line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_SETDDRAMADDR</span> 		<span class="o">=</span> <span class="mh">0x80</span></div><div class='line' id='LC22'><br/></div><div class='line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># flags for display entry mode</span></div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_ENTRYRIGHT</span> 		<span class="o">=</span> <span class="mh">0x00</span></div><div class='line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_ENTRYLEFT</span> 		<span class="o">=</span> <span class="mh">0x02</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_ENTRYSHIFTINCREMENT</span> 	<span class="o">=</span> <span class="mh">0x01</span></div><div class='line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_ENTRYSHIFTDECREMENT</span> 	<span class="o">=</span> <span class="mh">0x00</span></div><div class='line' id='LC28'><br/></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># flags for display on/off control</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_DISPLAYON</span> 		<span class="o">=</span> <span class="mh">0x04</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_DISPLAYOFF</span> 		<span class="o">=</span> <span class="mh">0x00</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_CURSORON</span> 		<span class="o">=</span> <span class="mh">0x02</span></div><div class='line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_CURSOROFF</span> 		<span class="o">=</span> <span class="mh">0x00</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_BLINKON</span> 		<span class="o">=</span> <span class="mh">0x01</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_BLINKOFF</span> 		<span class="o">=</span> <span class="mh">0x00</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># flags for display/cursor shift</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_DISPLAYMOVE</span> 		<span class="o">=</span> <span class="mh">0x08</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_CURSORMOVE</span> 		<span class="o">=</span> <span class="mh">0x00</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># flags for display/cursor shift</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_DISPLAYMOVE</span> 		<span class="o">=</span> <span class="mh">0x08</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_CURSORMOVE</span> 		<span class="o">=</span> <span class="mh">0x00</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_MOVERIGHT</span> 		<span class="o">=</span> <span class="mh">0x04</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_MOVELEFT</span> 		<span class="o">=</span> <span class="mh">0x00</span></div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># flags for function set</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_8BITMODE</span> 		<span class="o">=</span> <span class="mh">0x10</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_4BITMODE</span> 		<span class="o">=</span> <span class="mh">0x00</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_2LINE</span> 			<span class="o">=</span> <span class="mh">0x08</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_1LINE</span> 			<span class="o">=</span> <span class="mh">0x00</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_5x10DOTS</span> 		<span class="o">=</span> <span class="mh">0x04</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LCD_5x8DOTS</span> 		<span class="o">=</span> <span class="mh">0x00</span></div><div class='line' id='LC54'><br/></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'><br/></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">pin_rs</span><span class="o">=</span><span class="mi">25</span><span class="p">,</span> <span class="n">pin_e</span><span class="o">=</span><span class="mi">24</span><span class="p">,</span> <span class="n">pins_db</span><span class="o">=</span><span class="p">[</span><span class="mi">23</span><span class="p">,</span> <span class="mi">17</span><span class="p">,</span> <span class="mi">21</span><span class="p">,</span> <span class="mi">22</span><span class="p">],</span> <span class="n">GPIO</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC58'>	<span class="c"># Emulate the old behavior of using RPi.GPIO if we haven&#39;t been given</span></div><div class='line' id='LC59'>	<span class="c"># an explicit GPIO interface to use</span></div><div class='line' id='LC60'>	<span class="k">if</span> <span class="ow">not</span> <span class="n">GPIO</span><span class="p">:</span></div><div class='line' id='LC61'>	    <span class="kn">import</span> <span class="nn">RPi.GPIO</span> <span class="kn">as</span> <span class="nn">GPIO</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;	<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span> <span class="o">=</span> <span class="n">GPIO</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">pin_rs</span> <span class="o">=</span> <span class="n">pin_rs</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">pin_e</span> <span class="o">=</span> <span class="n">pin_e</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">pins_db</span> <span class="o">=</span> <span class="n">pins_db</span></div><div class='line' id='LC66'><br/></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span><span class="o">.</span><span class="n">setmode</span><span class="p">(</span><span class="n">GPIO</span><span class="o">.</span><span class="n">BCM</span><span class="p">)</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span><span class="o">.</span><span class="n">setup</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pin_e</span><span class="p">,</span> <span class="n">GPIO</span><span class="o">.</span><span class="n">OUT</span><span class="p">)</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span><span class="o">.</span><span class="n">setup</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pin_rs</span><span class="p">,</span> <span class="n">GPIO</span><span class="o">.</span><span class="n">OUT</span><span class="p">)</span></div><div class='line' id='LC70'><br/></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pin</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">pins_db</span><span class="p">:</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span><span class="o">.</span><span class="n">setup</span><span class="p">(</span><span class="n">pin</span><span class="p">,</span> <span class="n">GPIO</span><span class="o">.</span><span class="n">OUT</span><span class="p">)</span></div><div class='line' id='LC73'><br/></div><div class='line' id='LC74'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="mh">0x33</span><span class="p">)</span> <span class="c"># initialization</span></div><div class='line' id='LC75'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="mh">0x32</span><span class="p">)</span> <span class="c"># initialization</span></div><div class='line' id='LC76'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="mh">0x28</span><span class="p">)</span> <span class="c"># 2 line 5x7 matrix</span></div><div class='line' id='LC77'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="mh">0x0C</span><span class="p">)</span> <span class="c"># turn cursor off 0x0E to enable cursor</span></div><div class='line' id='LC78'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="mh">0x06</span><span class="p">)</span> <span class="c"># shift cursor right</span></div><div class='line' id='LC79'><br/></div><div class='line' id='LC80'>	<span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_DISPLAYON</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_CURSOROFF</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_BLINKOFF</span></div><div class='line' id='LC81'><br/></div><div class='line' id='LC82'>	<span class="bp">self</span><span class="o">.</span><span class="n">displayfunction</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_4BITMODE</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_1LINE</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_5x8DOTS</span></div><div class='line' id='LC83'>	<span class="bp">self</span><span class="o">.</span><span class="n">displayfunction</span> <span class="o">|=</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_2LINE</span></div><div class='line' id='LC84'><br/></div><div class='line' id='LC85'>	<span class="sd">&quot;&quot;&quot; Initialize to default text direction (for romance languages) &quot;&quot;&quot;</span></div><div class='line' id='LC86'>	<span class="bp">self</span><span class="o">.</span><span class="n">displaymode</span> <span class="o">=</span>  <span class="bp">self</span><span class="o">.</span><span class="n">LCD_ENTRYLEFT</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_ENTRYSHIFTDECREMENT</span></div><div class='line' id='LC87'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_ENTRYMODESET</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">displaymode</span><span class="p">)</span> <span class="c">#  set the entry mode</span></div><div class='line' id='LC88'><br/></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span></div><div class='line' id='LC90'><br/></div><div class='line' id='LC91'><br/></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">begin</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cols</span><span class="p">,</span> <span class="n">lines</span><span class="p">):</span></div><div class='line' id='LC93'><br/></div><div class='line' id='LC94'>	<span class="k">if</span> <span class="p">(</span><span class="n">lines</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC95'>		<span class="bp">self</span><span class="o">.</span><span class="n">numlines</span> <span class="o">=</span> <span class="n">lines</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;		<span class="bp">self</span><span class="o">.</span><span class="n">displayfunction</span> <span class="o">|=</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_2LINE</span></div><div class='line' id='LC97'>		<span class="bp">self</span><span class="o">.</span><span class="n">currline</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC98'><br/></div><div class='line' id='LC99'><br/></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">home</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC101'><br/></div><div class='line' id='LC102'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_RETURNHOME</span><span class="p">)</span> <span class="c"># set cursor position to zero</span></div><div class='line' id='LC103'>	<span class="bp">self</span><span class="o">.</span><span class="n">delayMicroseconds</span><span class="p">(</span><span class="mi">3000</span><span class="p">)</span> <span class="c"># this command takes a long time!</span></div><div class='line' id='LC104'><br/></div><div class='line' id='LC105'><br/></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC107'><br/></div><div class='line' id='LC108'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_CLEARDISPLAY</span><span class="p">)</span> <span class="c"># command to clear display</span></div><div class='line' id='LC109'>	<span class="bp">self</span><span class="o">.</span><span class="n">delayMicroseconds</span><span class="p">(</span><span class="mi">3000</span><span class="p">)</span>	<span class="c"># 3000 microsecond sleep, clearing the display takes a long time</span></div><div class='line' id='LC110'><br/></div><div class='line' id='LC111'><br/></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setCursor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">col</span><span class="p">,</span> <span class="n">row</span><span class="p">):</span></div><div class='line' id='LC113'><br/></div><div class='line' id='LC114'>	<span class="bp">self</span><span class="o">.</span><span class="n">row_offsets</span> <span class="o">=</span> <span class="p">[</span> <span class="mh">0x00</span><span class="p">,</span> <span class="mh">0x40</span><span class="p">,</span> <span class="mh">0x14</span><span class="p">,</span> <span class="mh">0x54</span> <span class="p">]</span></div><div class='line' id='LC115'><br/></div><div class='line' id='LC116'>	<span class="k">if</span> <span class="p">(</span> <span class="n">row</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">numlines</span> <span class="p">):</span> </div><div class='line' id='LC117'>		<span class="n">row</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">numlines</span> <span class="o">-</span> <span class="mi">1</span> <span class="c"># we count rows starting w/0</span></div><div class='line' id='LC118'><br/></div><div class='line' id='LC119'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_SETDDRAMADDR</span> <span class="o">|</span> <span class="p">(</span><span class="n">col</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">row_offsets</span><span class="p">[</span><span class="n">row</span><span class="p">]))</span></div><div class='line' id='LC120'><br/></div><div class='line' id='LC121'><br/></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">noDisplay</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span> </div><div class='line' id='LC123'>	<span class="sd">&quot;&quot;&quot; Turn the display off (quickly) &quot;&quot;&quot;</span></div><div class='line' id='LC124'><br/></div><div class='line' id='LC125'>	<span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span> <span class="o">&amp;=</span> <span class="o">~</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_DISPLAYON</span></div><div class='line' id='LC126'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_DISPLAYCONTROL</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span><span class="p">)</span></div><div class='line' id='LC127'><br/></div><div class='line' id='LC128'><br/></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">display</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC130'>	<span class="sd">&quot;&quot;&quot; Turn the display on (quickly) &quot;&quot;&quot;</span></div><div class='line' id='LC131'><br/></div><div class='line' id='LC132'>	<span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span> <span class="o">|=</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_DISPLAYON</span></div><div class='line' id='LC133'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_DISPLAYCONTROL</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span><span class="p">)</span></div><div class='line' id='LC134'><br/></div><div class='line' id='LC135'><br/></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">noCursor</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC137'>	<span class="sd">&quot;&quot;&quot; Turns the underline cursor on/off &quot;&quot;&quot;</span></div><div class='line' id='LC138'><br/></div><div class='line' id='LC139'>	<span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span> <span class="o">&amp;=</span> <span class="o">~</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_CURSORON</span></div><div class='line' id='LC140'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_DISPLAYCONTROL</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span><span class="p">)</span></div><div class='line' id='LC141'><br/></div><div class='line' id='LC142'><br/></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">cursor</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC144'>	<span class="sd">&quot;&quot;&quot; Cursor On &quot;&quot;&quot;</span></div><div class='line' id='LC145'><br/></div><div class='line' id='LC146'>	<span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span> <span class="o">|=</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_CURSORON</span></div><div class='line' id='LC147'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_DISPLAYCONTROL</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span><span class="p">)</span></div><div class='line' id='LC148'><br/></div><div class='line' id='LC149'><br/></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">noBlink</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC151'>	<span class="sd">&quot;&quot;&quot; Turn on and off the blinking cursor &quot;&quot;&quot;</span></div><div class='line' id='LC152'><br/></div><div class='line' id='LC153'>	<span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span> <span class="o">&amp;=</span> <span class="o">~</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_BLINKON</span></div><div class='line' id='LC154'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_DISPLAYCONTROL</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span><span class="p">)</span></div><div class='line' id='LC155'><br/></div><div class='line' id='LC156'><br/></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">noBlink</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC158'>	<span class="sd">&quot;&quot;&quot; Turn on and off the blinking cursor &quot;&quot;&quot;</span></div><div class='line' id='LC159'><br/></div><div class='line' id='LC160'>	<span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span> <span class="o">&amp;=</span> <span class="o">~</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_BLINKON</span></div><div class='line' id='LC161'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_DISPLAYCONTROL</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">displaycontrol</span><span class="p">)</span></div><div class='line' id='LC162'><br/></div><div class='line' id='LC163'><br/></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">DisplayLeft</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC165'>	<span class="sd">&quot;&quot;&quot; These commands scroll the display without changing the RAM &quot;&quot;&quot;</span></div><div class='line' id='LC166'><br/></div><div class='line' id='LC167'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_CURSORSHIFT</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_DISPLAYMOVE</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_MOVELEFT</span><span class="p">)</span></div><div class='line' id='LC168'><br/></div><div class='line' id='LC169'><br/></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">scrollDisplayRight</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC171'>	<span class="sd">&quot;&quot;&quot; These commands scroll the display without changing the RAM &quot;&quot;&quot;</span></div><div class='line' id='LC172'><br/></div><div class='line' id='LC173'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_CURSORSHIFT</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_DISPLAYMOVE</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_MOVERIGHT</span><span class="p">);</span></div><div class='line' id='LC174'><br/></div><div class='line' id='LC175'><br/></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">leftToRight</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC177'>	<span class="sd">&quot;&quot;&quot; This is for text that flows Left to Right &quot;&quot;&quot;</span></div><div class='line' id='LC178'><br/></div><div class='line' id='LC179'>	<span class="bp">self</span><span class="o">.</span><span class="n">displaymode</span> <span class="o">|=</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_ENTRYLEFT</span></div><div class='line' id='LC180'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_ENTRYMODESET</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">displaymode</span><span class="p">);</span></div><div class='line' id='LC181'><br/></div><div class='line' id='LC182'><br/></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">rightToLeft</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC184'>	<span class="sd">&quot;&quot;&quot; This is for text that flows Right to Left &quot;&quot;&quot;</span></div><div class='line' id='LC185'>	<span class="bp">self</span><span class="o">.</span><span class="n">displaymode</span> <span class="o">&amp;=</span> <span class="o">~</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_ENTRYLEFT</span></div><div class='line' id='LC186'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_ENTRYMODESET</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">displaymode</span><span class="p">)</span></div><div class='line' id='LC187'><br/></div><div class='line' id='LC188'><br/></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">autoscroll</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC190'>	<span class="sd">&quot;&quot;&quot; This will &#39;right justify&#39; text from the cursor &quot;&quot;&quot;</span></div><div class='line' id='LC191'><br/></div><div class='line' id='LC192'>	<span class="bp">self</span><span class="o">.</span><span class="n">displaymode</span> <span class="o">|=</span> <span class="bp">self</span><span class="o">.</span><span class="n">LCD_ENTRYSHIFTINCREMENT</span></div><div class='line' id='LC193'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_ENTRYMODESET</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">displaymode</span><span class="p">)</span></div><div class='line' id='LC194'><br/></div><div class='line' id='LC195'><br/></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">noAutoscroll</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span> </div><div class='line' id='LC197'>	<span class="sd">&quot;&quot;&quot; This will &#39;left justify&#39; text from the cursor &quot;&quot;&quot;</span></div><div class='line' id='LC198'><br/></div><div class='line' id='LC199'>	<span class="bp">self</span><span class="o">.</span><span class="n">displaymode</span> <span class="o">&amp;=</span> <span class="o">~</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_ENTRYSHIFTINCREMENT</span></div><div class='line' id='LC200'>	<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LCD_ENTRYMODESET</span> <span class="o">|</span> <span class="bp">self</span><span class="o">.</span><span class="n">displaymode</span><span class="p">)</span></div><div class='line' id='LC201'><br/></div><div class='line' id='LC202'><br/></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">write4bits</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">bits</span><span class="p">,</span> <span class="n">char_mode</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; Send command to LCD &quot;&quot;&quot;</span></div><div class='line' id='LC205'><br/></div><div class='line' id='LC206'>	<span class="bp">self</span><span class="o">.</span><span class="n">delayMicroseconds</span><span class="p">(</span><span class="mi">1000</span><span class="p">)</span> <span class="c"># 1000 microsecond sleep</span></div><div class='line' id='LC207'><br/></div><div class='line' id='LC208'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bits</span><span class="o">=</span><span class="nb">bin</span><span class="p">(</span><span class="n">bits</span><span class="p">)[</span><span class="mi">2</span><span class="p">:]</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">8</span><span class="p">)</span></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span><span class="o">.</span><span class="n">output</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pin_rs</span><span class="p">,</span> <span class="n">char_mode</span><span class="p">)</span></div><div class='line' id='LC211'><br/></div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pin</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">pins_db</span><span class="p">:</span></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span><span class="o">.</span><span class="n">output</span><span class="p">(</span><span class="n">pin</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC214'><br/></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">4</span><span class="p">):</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;1&quot;</span><span class="p">:</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span><span class="o">.</span><span class="n">output</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pins_db</span><span class="p">[::</span><span class="o">-</span><span class="mi">1</span><span class="p">][</span><span class="n">i</span><span class="p">],</span> <span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC218'><br/></div><div class='line' id='LC219'>	<span class="bp">self</span><span class="o">.</span><span class="n">pulseEnable</span><span class="p">()</span></div><div class='line' id='LC220'><br/></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pin</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">pins_db</span><span class="p">:</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span><span class="o">.</span><span class="n">output</span><span class="p">(</span><span class="n">pin</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC223'><br/></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span><span class="mi">8</span><span class="p">):</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;1&quot;</span><span class="p">:</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span><span class="o">.</span><span class="n">output</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pins_db</span><span class="p">[::</span><span class="o">-</span><span class="mi">1</span><span class="p">][</span><span class="n">i</span><span class="o">-</span><span class="mi">4</span><span class="p">],</span> <span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC227'><br/></div><div class='line' id='LC228'>	<span class="bp">self</span><span class="o">.</span><span class="n">pulseEnable</span><span class="p">()</span></div><div class='line' id='LC229'><br/></div><div class='line' id='LC230'><br/></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">delayMicroseconds</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">microseconds</span><span class="p">):</span></div><div class='line' id='LC232'>	<span class="n">seconds</span> <span class="o">=</span> <span class="n">microseconds</span> <span class="o">/</span> <span class="nb">float</span><span class="p">(</span><span class="mi">1000000</span><span class="p">)</span>	<span class="c"># divide microseconds by 1 million for seconds</span></div><div class='line' id='LC233'>	<span class="n">sleep</span><span class="p">(</span><span class="n">seconds</span><span class="p">)</span></div><div class='line' id='LC234'><br/></div><div class='line' id='LC235'><br/></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">pulseEnable</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC237'>	<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span><span class="o">.</span><span class="n">output</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pin_e</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC238'>	<span class="bp">self</span><span class="o">.</span><span class="n">delayMicroseconds</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>		<span class="c"># 1 microsecond pause - enable pulse must be &gt; 450ns </span></div><div class='line' id='LC239'>	<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span><span class="o">.</span><span class="n">output</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pin_e</span><span class="p">,</span> <span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC240'>	<span class="bp">self</span><span class="o">.</span><span class="n">delayMicroseconds</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>		<span class="c"># 1 microsecond pause - enable pulse must be &gt; 450ns </span></div><div class='line' id='LC241'>	<span class="bp">self</span><span class="o">.</span><span class="n">GPIO</span><span class="o">.</span><span class="n">output</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pin_e</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC242'>	<span class="bp">self</span><span class="o">.</span><span class="n">delayMicroseconds</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>		<span class="c"># commands need &gt; 37us to settle</span></div><div class='line' id='LC243'><br/></div><div class='line' id='LC244'><br/></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">):</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; Send string to LCD. Newline wraps to second line&quot;&quot;&quot;</span></div><div class='line' id='LC247'><br/></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">char</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">char</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">:</span></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="mh">0xC0</span><span class="p">)</span> <span class="c"># next line</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write4bits</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="n">char</span><span class="p">),</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC253'><br/></div><div class='line' id='LC254'><br/></div><div class='line' id='LC255'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line' id='LC256'><br/></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lcd</span> <span class="o">=</span> <span class="n">Adafruit_CharLCD</span><span class="p">()</span></div><div class='line' id='LC258'><br/></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lcd</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lcd</span><span class="o">.</span><span class="n">message</span><span class="p">(</span><span class="s">&quot;  Adafruit 16x2</span><span class="se">\n</span><span class="s">  Standard LCD&quot;</span><span class="p">)</span></div><div class='line' id='LC261'><br/></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;">
            <button type="submit" class="button">Go</button>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif" height="64" width="64">
</div>


        </div>
      </div>
      <div class="modal-backdrop"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="/about">About us</a></dd>
        <dd><a href="/blog">Blog</a></dd>
        <dd><a href="/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.09596s from fe4.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>
    <ul id="legal">
        <li><a href="/site/terms">Terms of Service</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/adafruit/Adafruit-Raspberry-Pi-Python-Code/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

    
    <span id='server_response_time' data-time='0.09665' data-host='fe4'></span>
    
  </body>
</html>

