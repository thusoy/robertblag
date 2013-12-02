module.exports = function(grunt) {

  // load grunt tasks from package.json
  require('load-grunt-tasks')(grunt);

  // Project configuration.
  grunt.initConfig({

    bower: {
      install: {
        options: {
          targetDir: 'bower_components',
        }
      }
    },

    clean: {
      dist: [
        '.tmp',
        'dist',
        'robert/**/*.pyc',
      ],
      postbuild: [
        'dist/static/sass',
        'dist/static/raw_img',
      ],
    },

    compass: {
      dist: {
        options: {
          sassDir: '.tmp/static/sass/',
          cssDir: 'robert/static/css/',
          outputStyle: 'compressed',
        }
      }
    },

    concurrent: {
      server: {
        options: {
          logConcurrentOutput: true,
        },
        tasks: ['watch', 'shell:devserver']
      }
    },

    copy: {
      bootstrap: {
        files: [{
          expand: true,
          cwd: 'bower_components/sass-bootstrap/lib',
          src: ['_*'],
          dest: '.tmp/static/sass/bootstrap',
        }]
      },
      robertSass: {
        files: [{
          expand: true,
          cwd: 'robert/static/sass',
          src: ['**'],
          dest: '.tmp/static/sass',
        }]
      }
    },

    shell: {
      options: {
        stdout: true,
        stderr: true,
      },
      devserver: {
        command: 'python run_devserver.py',
      },
      freeze: {
        command: 'python freeze.py',
      }
    },

    watch: {
      options: {
        livereload: true,
      },
      python: {
        files: ['robert/**/*.py'],
        tasks: []
      },
      sass: {
        files: ['robert/static/sass/*.scss'],
        tasks: ['compass'],
      },
      templates: {
        files: ['robert/templates/*.html'],
        tasks: [],
      },
      articles: {
        files: ['articles/*.md'],
        tasks: [],
      },
    },
  });

  grunt.registerTask('default', [
    'build',
    'concurrent:server',
  ]);

  grunt.registerTask('build', [
    'clean:dist',
    'copy',
    'compass',
    'shell:freeze',
    'clean:postbuild',
  ]);
};
