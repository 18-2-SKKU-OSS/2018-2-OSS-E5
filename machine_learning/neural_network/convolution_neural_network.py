#-*- coding: utf-8 -*-

'''
     - - - - - -- - - - - - - - - - - - - - - - - - - - - - -
    이름 - CNN - 사진 인식을위한 회선 신경망
     목표 - - 손으로 쓰기 Word Photo 작성하기
     Detail : 총 5 개의 레이어 신경 네트워크
             * 컨볼 루션 계층
             * 풀링 레이어
             * BP의 입력 레이어 레이어
             BP의 숨겨진 층
             * BP의 출력 레이어
    Author: Stephen Lee
    Github: 245885195@qq.com
    Date: 2017.9.20
    - - - - - -- - - - - - - - - - - - - - - - - - - - - - -
          '''
from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

class CNN():

    def __init__(self,conv1_get,size_p1,bp_num1,bp_num2,bp_num3,rate_w=0.2,rate_t=0.2):
        '''
         : param conv1_get : [a, c, d], 크기, 수, 회선 커널 단계
         : param size_p1 : 풀링 크기
         : param bp_num1 : 평평한 레이어의 단위 수
         : 매개 변수 bp_num2 : 숨겨진 레이어의 단위 수
         : param bp_num3 : 출력 레이어의 단위 수
         : param rate_w : 가중치 학습의 비율
         : param rate_t : 임계 값 학습 속도
        '''
        self.num_bp1 = bp_num1
        self.num_bp2 = bp_num2
        self.num_bp3 = bp_num3
        self.conv1 = conv1_get[:2]
        self.step_conv1 = conv1_get[2]
        self.size_pooling1 = size_p1
        self.rate_weight = rate_w
        self.rate_thre = rate_t
        self.w_conv1 = [np.mat(-1*np.random.rand(self.conv1[0],self.conv1[0])+0.5) for i in range(self.conv1[1])]
        self.wkj = np.mat(-1 * np.random.rand(self.num_bp3, self.num_bp2) + 0.5)
        self.vji = np.mat(-1*np.random.rand(self.num_bp2, self.num_bp1)+0.5)
        self.thre_conv1 = -2*np.random.rand(self.conv1[1])+1
        self.thre_bp2 = -2*np.random.rand(self.num_bp2)+1
        self.thre_bp3 = -2*np.random.rand(self.num_bp3)+1


    def save_model(self,save_path):
        # 피클로 모델 사전 저장
        import pickle
        model_dic = {'num_bp1':self.num_bp1,
                    'num_bp2':self.num_bp2,
                    'num_bp3':self.num_bp3,
                    'conv1':self.conv1,
                    'step_conv1':self.step_conv1,
                    'size_pooling1':self.size_pooling1,
                    'rate_weight':self.rate_weight,
                    'rate_thre':self.rate_thre,
                    'w_conv1':self.w_conv1,
                    'wkj':self.wkj,
                    'vji':self.vji,
                    'thre_conv1':self.thre_conv1,
                    'thre_bp2':self.thre_bp2,
                     'thre_bp3':self.thre_bp3}
        with open(save_path, 'wb') as f:
            pickle.dump(model_dic, f)

        print('Model saved： %s'% save_path)

    @classmethod
    def ReadModel(cls,model_path):
        #저장된 모델 읽기
        import pickle
        with open(model_path, 'rb') as f:
            model_dic = pickle.load(f)

        conv_get= model_dic.get('conv1')
        conv_get.append(model_dic.get('step_conv1'))
        size_p1 = model_dic.get('size_pooling1')
        bp1 = model_dic.get('num_bp1')
        bp2 = model_dic.get('num_bp2')
        bp3 = model_dic.get('num_bp3')
        r_w = model_dic.get('rate_weight')
        r_t = model_dic.get('rate_thre')
        # 모델 인스턴스 생성
        conv_ins = CNN(conv_get,size_p1,bp1,bp2,bp3,r_w,r_t)
        # 모델 매개 변수 수정
        conv_ins.w_conv1 = model_dic.get('w_conv1')
        conv_ins.wkj = model_dic.get('wkj')
        conv_ins.vji = model_dic.get('vji')
        conv_ins.thre_conv1 = model_dic.get('thre_conv1')
        conv_ins.thre_bp2 = model_dic.get('thre_bp2')
        conv_ins.thre_bp3 = model_dic.get('thre_bp3')
        return conv_ins


    def sig(self,x):
        return 1 / (1 + np.exp(-1*x))

    def do_round(self,x):
        return round(x, 3)

    def convolute(self,data,convs,w_convs,thre_convs,conv_step):
        #컨벌루션 프로세스
        size_conv = convs[0]
        num_conv =convs[1]
        size_data = np.shape(data)[0]
        #원본 이미지 데이터의 데이터 조각을 가져온다. data_focus
        data_focus = []
        for i_focus in range(0, size_data - size_conv + 1, conv_step):
            for j_focus in range(0, size_data - size_conv + 1, conv_step):
                focus = data[i_focus:i_focus + size_conv, j_focus:j_focus + size_conv]
                data_focus.append(focus)
        #모든 단일 커널의 특성지도를 계산하고 매트릭스 목록으로 저장
        data_featuremap = []
        Size_FeatureMap = int((size_data - size_conv) / conv_step + 1)
        for i_map in range(num_conv):
            featuremap = []
            for i_focus in range(len(data_focus)):
                net_focus = np.sum(np.multiply(data_focus[i_focus], w_convs[i_map])) - thre_convs[i_map]
                featuremap.append(self.sig(net_focus))
            featuremap = np.asmatrix(featuremap).reshape(Size_FeatureMap, Size_FeatureMap)
            data_featuremap.append(featuremap)

        #데이터 슬라이스를 One 차원으로 확장
        focus1_list = []
        for each_focus in data_focus:
            focus1_list.extend(self.Expand_Mat(each_focus))
        focus_list = np.asarray(focus1_list)
        return focus_list,data_featuremap

    def pooling(self,featuremaps,size_pooling,type='average_pool'):
        #풀링 프로세스
        size_map = len(featuremaps[0])
        size_pooled = int(size_map/size_pooling)
        featuremap_pooled = []
        for i_map in range(len(featuremaps)):
            map = featuremaps[i_map]
            map_pooled = []
            for i_focus in range(0,size_map,size_pooling):
                for j_focus in range(0, size_map, size_pooling):
                    focus = map[i_focus:i_focus + size_pooling, j_focus:j_focus + size_pooling]
                    if type == 'average_pool':
                        #평균 풀링
                        map_pooled.append(np.average(focus))
                    elif type == 'max_pooling':
                        #풀링 맥시멈
                        map_pooled.append(np.max(focus))
            map_pooled = np.asmatrix(map_pooled).reshape(size_pooled,size_pooled)
            featuremap_pooled.append(map_pooled)
        return featuremap_pooled

    def _expand(self,datas):
        #3 차원 데이터를 하나의 차원 목록으로 확장
        data_expanded = []
        for i in range(len(datas)):
            shapes = np.shape(datas[i])
            data_listed = datas[i].reshape(1,shapes[0]*shapes[1])
            data_listed = data_listed.getA().tolist()[0]
            data_expanded.extend(data_listed)
        data_expanded = np.asarray(data_expanded)
        return data_expanded

    def _expand_mat(self,data_mat):
        #행렬을 하나의 차원 목록으로 확장
        data_mat = np.asarray(data_mat)
        shapes = np.shape(data_mat)
        data_expanded = data_mat.reshape(1,shapes[0]*shapes[1])
        return data_expanded

    def _calculate_gradient_from_pool(self,out_map,pd_pool,num_map,size_map,size_pooling):
        '''
         풀 레이어의 데이터 슬라이스에서 그래디언트 계산
         pd_pool : 행렬의리스트
         out_map : 데이터 슬라이스의 모양 (size_map * size_map)
         반환 : pd_all : 매트릭스 목록, [num, size_map, size_map]
        '''
        pd_all = []
        i_pool = 0
        for i_map in range(num_map):
            pd_conv1 = np.ones((size_map, size_map))
            for i in range(0, size_map, size_pooling):
                for j in range(0, size_map, size_pooling):
                    pd_conv1[i:i + size_pooling, j:j + size_pooling] = pd_pool[i_pool]
                    i_pool = i_pool + 1
            pd_conv2 = np.multiply(pd_conv1,np.multiply(out_map[i_map],(1-out_map[i_map])))
            pd_all.append(pd_conv2)
        return pd_all

    def trian(self,patterns,datas_train, datas_teach, n_repeat, error_accuracy,draw_e = bool):
        # 모델 training
        print('----------------------Start Training-------------------------')
        print((' - - Shape: Train_Data  ',np.shape(datas_train)))
        print((' - - Shape: Teach_Data  ',np.shape(datas_teach)))
        rp = 0
        all_mse = []
        mse  = 10000
        while rp < n_repeat and mse >= error_accuracy:
            alle = 0
            print('-------------Learning Time %d--------------'%rp)
            for p in range(len(datas_train)):
                #print('------------Learning Image: %d--------------'%p)
                data_train = np.asmatrix(datas_train[p])
                data_teach = np.asarray(datas_teach[p])
                data_focus1,data_conved1 = self.convolute(data_train,self.conv1,self.w_conv1,
                                           self.thre_conv1,conv_step=self.step_conv1)
                data_pooled1 = self.pooling(data_conved1,self.size_pooling1)
                shape_featuremap1 = np.shape(data_conved1)
                '''
                print('  -----original shape   ', np.shape(data_train))
                print('  ---- after convolution  ',np.shape(data_conv1))
                print('  -----after pooling  ',np.shape(data_pooled1))
               '''
                data_bp_input = self._expand(data_pooled1)
                bp_out1 = data_bp_input

                bp_net_j = np.dot(bp_out1,self.vji.T) - self.thre_bp2
                bp_out2 = self.sig(bp_net_j)
                bp_net_k = np.dot(bp_out2 ,self.wkj.T) - self.thre_bp3
                bp_out3 = self.sig(bp_net_k)

                #--------------모델 learning ------------------------
                #--------------오류 및 기울기 계산---------------
                pd_k_all = np.multiply((data_teach - bp_out3), np.multiply(bp_out3, (1 - bp_out3)))
                pd_j_all = np.multiply(np.dot(pd_k_all,self.wkj), np.multiply(bp_out2, (1 - bp_out2)))
                pd_i_all = np.dot(pd_j_all,self.vji)

                pd_conv1_pooled = pd_i_all / (self.size_pooling1*self.size_pooling1)
                pd_conv1_pooled = pd_conv1_pooled.T.getA().tolist()
                pd_conv1_all = self._calculate_gradient_from_pool(data_conved1,pd_conv1_pooled,shape_featuremap1[0],
                                                    shape_featuremap1[1],self.size_pooling1)
                #가중치 및 임계 값 학습 과정---------
                #회선 층------------------------
                for k_conv in range(self.conv1[1]):
                    pd_conv_list = self._expand_mat(pd_conv1_all[k_conv])
                    delta_w = self.rate_weight * np.dot(pd_conv_list,data_focus1)

                    self.w_conv1[k_conv] = self.w_conv1[k_conv] + delta_w.reshape((self.conv1[0],self.conv1[0]))

                    self.thre_conv1[k_conv] = self.thre_conv1[k_conv] - np.sum(pd_conv1_all[k_conv]) * self.rate_thre
                # 모든 연결된 층
                self.wkj = self.wkj + pd_k_all.T * bp_out2 * self.rate_weight
                self.vji = self.vji + pd_j_all.T * bp_out1 * self.rate_weight
                self.thre_bp3 = self.thre_bp3 - pd_k_all * self.rate_thre
                self.thre_bp2 = self.thre_bp2 - pd_j_all * self.rate_thre
                # 모든 단일 이미지의 합계 오차를 계산한다.
                errors = np.sum(abs((data_teach - bp_out3)))
                alle = alle + errors
                #print('   ----Teach      ',data_teach)
                #print('   ----BP_output  ',bp_out3)
            rp = rp + 1
            mse = alle/patterns
            all_mse.append(mse)
        def draw_error():
            yplot = [error_accuracy for i in range(int(n_repeat * 1.2))]
            plt.plot(all_mse, '+-')
            plt.plot(yplot, 'r--')
            plt.xlabel('Learning Times')
            plt.ylabel('All_mse')
            plt.grid(True, alpha=0.5)
            plt.show()
        print('------------------Training Complished---------------------')
        print((' - - Training epoch: ', rp, '     - - Mse: %.6f' % mse))
        if draw_e:
            draw_error()
        return mse

    def predict(self,datas_test):
        #model predict
        produce_out = []
        print('-------------------Start Testing-------------------------')
        print((' - - Shape: Test_Data  ',np.shape(datas_test)))
        for p in range(len(datas_test)):
            data_test = np.asmatrix(datas_test[p])
            data_focus1, data_conved1 = self.convolute(data_test, self.conv1, self.w_conv1,
                                                     self.thre_conv1, conv_step=self.step_conv1)
            data_pooled1 = self.pooling(data_conved1, self.size_pooling1)
            data_bp_input = self._expand(data_pooled1)

            bp_out1 = data_bp_input
            bp_net_j = bp_out1 * self.vji.T - self.thre_bp2
            bp_out2 = self.sig(bp_net_j)
            bp_net_k = bp_out2 * self.wkj.T - self.thre_bp3
            bp_out3 = self.sig(bp_net_k)
            produce_out.extend(bp_out3.getA().tolist())
        res = [list(map(self.do_round,each)) for each in produce_out]
        return np.asarray(res)

    def convolution(self,data):
        # 체크 아웃 할 수 있도록 프로세스를 뒤얽힌 후 이미지의 데이터를 반환
        data_test = np.asmatrix(data)
        data_focus1, data_conved1 = self.convolute(data_test, self.conv1, self.w_conv1,
                                                     self.thre_conv1, conv_step=self.step_conv1)
        data_pooled1 = self.pooling(data_conved1, self.size_pooling1)

        return data_conved1,data_pooled1


if __name__ == '__main__':
    pass
    '''
    put the example on other file
    '''
